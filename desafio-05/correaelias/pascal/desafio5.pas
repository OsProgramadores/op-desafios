{
  Solução do desafio 5 em Pascal por Elias Correa (Jan/2019)
  
  Download freepascal compiler (fpc) here https://www.freepascal.org/ or thru your distro package manager
  
  Compile with:
  fpc desafio5.pas -O4
}

program Desafio5;

{$MODE OBJFPC}

uses
  {$ifdef unix}
  cthreads,
  cmem, // the c memory manager is on some systems much faster for multi-threading
  {$endif}
  SysUtils, Classes, Contnrs;

const
  BufferLength = 1024 * 1024 * 8; //amount of data each thread will work out from file (in Bytes)

type
  
  TArea = record
    FName: ShortString;
    FTotalEmployees: LongInt;
    FTotalSalary: Int64;
    FMinSalary, FMaxSalary: Int64;
    FMinNames, FMaxNames: TStringList;
  end;
  
  PArea = ^TArea;
  
  TSurname = record
    FTotalEmployees: LongInt;
    FMaxSalary: Int64;
    FMaxNames: TStringList;
  end;
  
  PSurname = ^TSurname;
  
  TThreadData = record
    FBuffer: array[0 .. BufferLength - 1] of Char;
    FTotalEmployees: LongInt;
    FTotalSalary: Int64;
    FMinSalary, FMaxSalary: Int64;
    FMinNames, FMaxNames: TStringList;
    FAreas, FSurnames: TFPHashList;
  end;
  
  PThreadData = ^TThreadData;

function ConcatNames(AName, ASurname: PShortString): ShortString; Inline;
begin
  if (AName <> nil) and (ASurname <> nil) then
  begin
    SetLength(Result, Length(AName^) + Length(ASurname^) + 1);
    Move(AName^[1], Result[1], Length(AName^));
    Result[Length(AName^) + 1] := ' ';
    Move(ASurname^[1], Result[Length(AName^) + 2], Length(ASurname^));
  end
  else
  begin
    Result := AName^;
  end;
end;

procedure AppendNameList(var ANameList: TStringList; var AListSalary: Int64; AName, ASurname: PShortString; ASalary: Int64; AKeepMinSalary: Boolean); inline;
begin
  if ANameList = nil then ANameList := TStringList.Create;
  if AListSalary = ASalary then
  begin
    ANameList.Append(ConcatNames(AName, ASurname));
  end
  else if (AListSalary = 0) or
          (AKeepMinSalary and (ASalary < AListSalary)) or
          ((not AKeepMinSalary) and (ASalary > AListSalary)) then
  begin
    AListSalary := ASalary;
    ANameList.Clear;
    ANameList.Append(ConcatNames(AName, ASurname));
  end;
end;

procedure JoinNameList(const ASourceList: TStringList; var ADestList: TStringList; ASourceSalary: Int64; var ADestSalary: Int64; AKeepMinSalary: Boolean); inline;
begin
  if ASourceList = nil then exit;
  if ADestList = nil then ADestList := TStringList.Create;
  if ASourceSalary = ADestSalary then
  begin
    ADestList.AddStrings(ASourceList);
  end
  else if (ADestSalary = 0) or
          (AKeepMinSalary and (ASourceSalary < ADestSalary)) or
          ((not AKeepMinSalary) and (ASourceSalary > ADestSalary)) then
  begin
    ADestSalary := ASourceSalary;
    ADestList.Clear;
    ADestList.AddStrings(ASourceList);
  end;
end;

function GetItem(var AList: TFPHashList; const AName: ShortString; ASize: SizeInt): Pointer; inline;
var
  Item: Pointer;
begin
  Item := AList.Find(AName);
  if Item = nil then
  begin
    Item := GetMem(ASize);
    FillChar(Item^, ASize, 0);
    AList.Add(AName, Item);
  end;
  Result := Item;
end;

procedure LoadJsonChunk(var JsonFile: TFileStream; ABuffer: PChar);
var
  Len: SizeInt;
begin
  Len := JsonFile.Read(ABuffer^, BufferLength - 1);
  
  //rewind file until a '}' is found, reading only complete objects
  if JsonFile.Position <> JsonFile.Size then
  begin
    while ABuffer[Len - 1] <> '}' do
    begin
      Dec(Len);
      JsonFile.Position := JsonFile.Position - 1;
    end;
  end;
  
  //null terminated
  ABuffer[Len] := #0;
end;

function GetString(var ABuffer: PChar): PShortString; inline;
var
  Start: PChar = nil;
  C: PChar;
begin
  C := ABuffer;
  
  while (C^ <> #0) and (C^ <> '"') do Inc(C);
  if C^ = '"' then
  begin
    Start := C;
    Inc(C); //skip '"'
  end;
  
  while (C^ <> #0) and (C^ <> '"') do Inc(C);
  
  if C^ = '"' then
  begin
    if Start <> nil then
      Start[0] := Char(C - Start - 1); //store length in the 0 index (short pascal strings)
    Inc(C); //skip '"'
  end;
  
  Result := PShortString(Start);
  
  ABuffer := C;
end;

function GetNumber(var ABuffer: PChar): Int64; inline;
var
  C: PChar;
begin
  Result := 0;

  C := ABuffer;

  while (C^ <> #0) and (not (C^ in ['0'..'9', '.'])) do Inc(C);
  
  while C^ in ['0'..'9', '.'] do
  begin
    if C^ <> '.' then
      Result := Result * 10 + (LongInt(C^) - LongInt('0'));
    Inc(C);
  end;
  
  ABuffer := C;
end;

procedure ParseJsonChunk(ABuffer: PChar; var AData: TThreadData);
var
  C: PChar;
  Name, Surname, Code: PShortString;
  Salary: Int64;
begin
  C := ABuffer;
  
  while C^ <> #0 do
  begin
    //find a property
    while (C^ <> #0) and (C^ <> '"') do Inc(C);
    if C^ = '"' then Inc(C); //skip '"'
    
    //employee (starts with i of id)
    if C^ = 'i' then
    begin
      //ignore id
      while (C^ <> #0) and (C^ <> ',') do Inc(C);
      
      //get name
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Name := GetString(C);
      
      //get surname
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Surname := GetString(C);
      
      //get salary
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Salary := GetNumber(C);
      
      //get area
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Code := GetString(C);
      
      //update global counters
      Inc(AData.FTotalEmployees);
      AData.FTotalSalary += Salary;
      AppendNameList(AData.FMinNames, AData.FMinSalary, Name, Surname, Salary, True);
      AppendNameList(AData.FMaxNames, AData.FMaxSalary, Name, Surname, Salary, False);
      
      //update areas
      with PArea(GetItem(AData.FAreas, Code^, SizeOf(TArea)))^ do
      begin
        Inc(FTotalEmployees);
        FTotalSalary += Salary;
        AppendNameList(FMinNames, FMinSalary, Name, Surname, Salary, True);
        AppendNameList(FMaxNames, FMaxSalary, Name, Surname, Salary, False);
      end;
      
      //update surnames
      with PSurname(GetItem(AData.FSurnames, Surname^, SizeOf(TSurname)))^ do
      begin
        Inc(FTotalEmployees);
        AppendNameList(FMaxNames, FMaxSalary, Name, nil, Salary, False);
      end;
    end
    //area (starts with c of code)
    else if C^ = 'c' then //area
    begin
      //get code
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Code := GetString(C);
      
      //get name
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      Name := GetString(C);
      
      //set area name
      PArea(GetItem(AData.FAreas, Code^, SizeOf(TArea)))^.FName := Name^;
    end;
  end;
end;

var
  CriticalSection: TRTLCriticalSection;
  EmployeeFile: TFileStream;

procedure ThreadProc(AData: Pointer);
begin
  TThread.CurrentThread.FreeOnTerminate := False;
  
  while not TThread.CurrentThread.CheckTerminated do
  begin
    EnterCriticalSection(CriticalSection);
      if EmployeeFile.Position = EmployeeFile.Size then
        TThread.CurrentThread.Terminate;
      LoadJsonChunk(EmployeeFile, @(PThreadData(AData)^.FBuffer[0]));
    LeaveCriticalSection(CriticalSection);
    
    ParseJsonChunk(@(PThreadData(AData)^.FBuffer[0]), PThreadData(AData)^);
  end;
end;

var
  Threads: array of TThread;
  Data: array of TThreadData;
  
  I, J: LongInt;
  
  MostEmployees: LongInt = 0;
  LeastEmployees: LongInt = High(LongInt);
  
  AreaInfo: PArea;
  SurnameInfo: PSurname;
begin
  //check command line params
  if ParamCount <> 1 then
  begin
    WriteLn('Usage: ', ParamStr(0), ' <input file>');
    Halt(1);
  end;
  
  FormatSettings.DecimalSeparator := '.';
  
  SetLength(Threads, TThread.ProcessorCount);
  SetLength(Data, TThread.ProcessorCount);
  
  //init thread data
  for I := 0 to High(Data) do
  begin
    with Data[I] do
    begin
      FMinNames := TStringList.Create;
      FMaxNames := TStringList.Create;
      FAreas := TFPHashList.Create;
      FSurnames := TFPHashList.Create;
    end;
  end;
  
  InitCriticalSection(CriticalSection);
  
  EmployeeFile := TFileStream.Create(ParamStr(1), fmOpenRead or fmShareDenyWrite);
  
  for I := 0 to High(Threads) do
  begin
    Threads[I] := TThread.ExecuteInThread(@ThreadProc, @Data[I]);
    Threads[I].Priority := tpTimeCritical;
  end;
    
  for I := 0 to High(Threads) do
  begin
    Threads[I].WaitFor;
    Threads[I].Free;
  end;
  
  EmployeeFile.Free;
  
  DoneCriticalSection(CriticalSection);
  
  //join results
  with Data[0] do
  begin
    for I := 1 to High(Data) do
    begin
      //global
      FTotalEmployees += Data[I].FTotalEmployees;
      FTotalSalary += Data[I].FTotalSalary;
      JoinNameList(Data[I].FMinNames, FMinNames, Data[I].FMinSalary, FMinSalary, True);
      JoinNameList(Data[I].FMaxNames, FMaxNames, Data[I].FMaxSalary, FMaxSalary, False);
      
      //areas
      for J := 0 to Data[I].FAreas.Count - 1 do
      begin
        AreaInfo := Data[I].FAreas.Items[J];
        with PArea(GetItem(FAreas, Data[I].FAreas.NameOfIndex(J), SizeOf(TArea)))^ do
        begin
          if Length(AreaInfo^.FName) <> 0 then FName := AreaInfo^.FName;
          FTotalEmployees += AreaInfo^.FTotalEmployees;
          FTotalSalary += AreaInfo^.FTotalSalary;
          JoinNameList(AreaInfo^.FMinNames, FMinNames, AreaInfo^.FMinSalary, FMinSalary, True);
          JoinNameList(AreaInfo^.FMaxNames, FMaxNames, AreaInfo^.FMaxSalary, FMaxSalary, False);
        end;
      end;
      
      //surnames
      for J := 0 to Data[I].FSurnames.Count - 1 do
      begin
        SurnameInfo := Data[I].FSurnames.Items[J];
        with PSurname(GetItem(FSurnames, Data[I].FSurnames.NameOfIndex(J), SizeOf(TSurname)))^ do
        begin
          FTotalEmployees += SurnameInfo^.FTotalEmployees;
          JoinNameList(SurnameInfo^.FMaxNames, FMaxNames, SurnameInfo^.FMaxSalary, FMaxSalary, False);
        end;
      end;
    end;
  end;
  
  //print results
  
  //global
  with Data[0] do
  begin
    for I := 0 to FMinNames.Count - 1 do
      WriteLn('global_min|', FMinNames[I], '|', (FMinSalary * 0.01):0:2);
    
    for I := 0 to FMaxNames.Count - 1 do
      WriteLn('global_max|', FMaxNames[I], '|', (FMaxSalary * 0.01):0:2);
    
    WriteLn('global_avg|', ((FTotalSalary * 0.01) / FTotalEmployees):0:2);
  end;
  
  //areas
  for I := 0 to Data[0].FAreas.Count - 1 do
  begin
    with PArea(Data[0].FAreas.Items[I])^ do
    begin
      if FTotalEmployees > 0 then
      begin
        WriteLn('area_avg|', FName, '|', ((FTotalSalary * 0.01) / FTotalEmployees):0:2);
        
        for J := 0 to FMinNames.Count - 1 do
          WriteLn('area_min|', FName, '|', FMinNames[J], '|', (FMinSalary * 0.01):0:2);
        
        for J := 0 to FMaxNames.Count - 1 do
          WriteLn('area_max|', FName, '|', FMaxNames[J], '|', (FMaxSalary * 0.01):0:2);
        
        if FTotalEmployees > MostEmployees then
          MostEmployees := FTotalEmployees;
        
        if (FTotalEmployees > 0) and (FTotalEmployees < LeastEmployees) then
          LeastEmployees := FTotalEmployees;
      end;
    end;
  end;
  
  for I := 0 to Data[0].FAreas.Count - 1 do
  begin
    with PArea(Data[0].FAreas.Items[I])^ do
    begin
      if FTotalEmployees = MostEmployees then
        WriteLn('most_employees|', FName, '|', FTotalEmployees);
      
      if FTotalEmployees = LeastEmployees then
        WriteLn('least_employees|', FName, '|', FTotalEmployees);
    end;
  end;

  //surnames
  for I := 0 to Data[0].FSurnames.Count - 1 do
  begin
    with PSurname(Data[0].FSurnames.Items[I])^ do
      if FTotalEmployees > 1 then
        for J := 0 to FMaxNames.Count - 1 do
          WriteLn('last_name_max|', Data[0].FSurnames.NameOfIndex(I), '|', FMaxNames[J], ' ', Data[0].FSurnames.NameOfIndex(I), '|', (Double(FMaxSalary) * Double(0.01)):0:2);
  end;
end.