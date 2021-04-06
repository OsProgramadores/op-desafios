{
Compile with Free Pascal Compiler (FPC):
fpc desafio5.pas -O4
}

program Desafio5;

{$mode objfpc}
{$inline on}

uses 
  {$ifdef unix}
  Cthreads,
  CMem, //the c memory manager is on some systems much faster for multi-threading
  {$endif}
  SysUtils, Classes, Contnrs, StrUtils, Math;

type
  TArea = record
    FName: PShortString;
    FTotalEmployees: LongInt;
    FTotalSalary: Int64;
    FMinSalary, FMaxSalary: Int64;
    FMinNames, FMaxNames: TFPList;
  end;
  
  PArea = ^TArea;
  
  TSurname = record
    FTotalEmployees: LongInt;
    FMaxSalary: Int64;
    FMaxNames: TFPList;
  end;
  
  PSurname = ^TSurname;
  
  TThreadData = record
    FBuffer: AnsiString;
    FTotalEmployees: LongInt;
    FTotalSalary: Int64;
    FMinSalary, FMaxSalary: Int64;
    FMinNames, FMaxNames: TFPList;
    FAreas, FSurnames: TFPHashList;
  end;

  PThreadData = ^TThreadData;

function GetArea(var AAreaList: TFPHashList; ACode: PShortString): PArea; inline;
begin
  Result := AAreaList.Find(ACode^);
  if Result = nil then
  begin
    Result := GetMem(SizeOf(TArea));
    with Result^ do
    begin
      FName := nil;
      FTotalEmployees := 0;
      FTotalSalary := 0;
      FMinSalary := 0;
      FMaxSalary := 0;
      FMinNames := TFPList.Create;
      FMaxNames := TFPList.Create;
    end;
    AAreaList.Add(ACode^, Result);
  end;
end;

function GetSurname(var ASurnameList: TFPHashList; const ASurname: PShortString): PSurname; inline;
begin
  Result := ASurnameList.Find(ASurname^);
  if Result = nil then
  begin
    Result := GetMem(SizeOf(TSurname));
    with Result^ do
    begin
      FTotalEmployees := 0;
      FMaxSalary := 0;
      FMaxNames := TFPList.Create;
    end;
    ASurnameList.Add(ASurname^, Result);
  end;
end;

procedure JoinNameList(const ASourceList: TFPList; var ADestList: TFPList; ASourceSalary: Int64; var ADestSalary: Int64; AKeepMinSalary: Boolean);
begin
  if ASourceSalary = ADestSalary then
  begin
    ADestList.AddList(ASourceList);
  end
  else if (ADestSalary = 0) or
          (AKeepMinSalary and (ASourceSalary < ADestSalary)) or
          ((not AKeepMinSalary) and (ASourceSalary > ADestSalary)) then
  begin
    ADestSalary := ASourceSalary;
    ADestList.Clear;
    ADestList.AddList(ASourceList);
  end;
end;

procedure ParseJsonChunk(var AData: TThreadData);
var
  Index: SizeInt = 0;
  Name, Surname, Code: PShortString;
  Salary: Int64;
  function GetString(): PShortString; inline;
  var
    Start: SizeInt;
  begin
    with AData do
    begin
      Index := PosEx(':', FBuffer, Index + 1);
      Index := PosEx('"', FBuffer, Index + 1);
      Start := Index;
      Index := PosEx('"', FBuffer, Index + 1);
      FBuffer[Start] := Chr(Index - Start - 1);
      Result := @FBuffer[Start];
    end;
  end;
  function GetNumber(): Int64; inline;
  var
    Start: SizeInt;
    C: Char;
  begin
    Result := 0;
    with AData do
    begin
      Start := Index + 1;
      Index := PosEx('.', FBuffer, Index + 1);
      Inc(Index, 3);
      while Start < Index do
      begin
        C := FBuffer[Start];
        if C <> '.' then
          Result := Result * 10 + (Ord(C) - Ord('0'));
        Inc(Start);
      end;
    end;
  end;
  procedure AddName(var AList: TFPList; var AListSalary: Int64; AName, ASurname: PShortString; ASalary: Int64; AKeepMinSalary: Boolean); inline;
  begin
    if AListSalary = ASalary then
    begin
      AList.Add(AName);
      if ASurname <> nil then AList.Add(ASurname);
    end
    else if (AListSalary = 0) or
            (AKeepMinSalary and (ASalary < AListSalary)) or
            ((not AKeepMinSalary) and (ASalary > AListSalary)) then
    begin
      AListSalary := ASalary;
      AList.Clear;
      AList.Add(AName);
      if ASurname <> nil then AList.Add(ASurname);
    end;
  end;
begin
  repeat
    Index := PosEx('"', AData.FBuffer, Index + 1);
    case AData.FBuffer[Index + 1] of
      'i': //employee (starts with i of id)
      begin
        //ignore id
        Inc(Index, 2);
        Index := PosEx(',', AData.FBuffer, Index + 1);
        
        //get name
        Inc(Index, 6);
        Name := GetString();
        
        //get surname
        Inc(Index, 11);
        Surname := GetString();
        
        //get salary
        Inc(Index, 9);
        Index := PosEx(':', AData.FBuffer, Index + 1);
        Salary := GetNumber();
        
        //get area
        Inc(Index, 6);
        Code := GetString();
        
        //updata global counters
        AData.FTotalSalary += Salary;
        Inc(AData.FTotalEmployees);
        AddName(AData.FMinNames, AData.FMinSalary, Name, Surname, Salary, True);
        AddName(AData.FMaxNames, AData.FMaxSalary, Name, Surname, Salary, False);
        
        //update areas
        with GetArea(AData.FAreas, Code)^ do
        begin
          Inc(FTotalEmployees);
          FTotalSalary += Salary;
          AddName(FMinNames, FMinSalary, Name, Surname, Salary, True);
          AddName(FMaxNames, FMaxSalary, Name, Surname, Salary, False);
        end;
        
        //update surnames
        with GetSurname(AData.FSurnames, Surname)^ do
        begin
          Inc(FTotalEmployees);
          AddName(FMaxNames, FMaxSalary, Name, nil, Salary, False);
        end;
      end;
      'c': //area (starts with c of code)
      begin
        //get code
        Inc(Index, 6);
        Code := GetString();
        
        //get name
        Inc(Index, 6);
        Name := GetString();
        
        //set area name
        GetArea(AData.FAreas, Code)^.FName := Name;
      end;
    end;
  until Index = 0;
end;

procedure ThreadProc(AData: Pointer);
begin
  TThread.CurrentThread.FreeOnTerminate := False;
  
  ParseJsonChunk(PThreadData(AData)^);
end;

var
  FilePath: AnsiString;
  FileStream: TFileStream;
  I, J: Integer;
  BufferSize, ReadSize: Int64;
  Threads: array of TThread;
  Data: array of TThreadData;
  CurrentArea: PArea;
  MostEmployees: LongInt = 0;
  LeastEmployees: LongInt = High(LongInt);
  CurrentSurname: PSurname;
  Key: ShortString;
  Cores: Int32 = 16;
begin
  if ParamCount < 1 then
  begin
    WriteLn('Usage: ', ParamStr(0), ' <input file> <thread_count>');
    Halt(1);
  end;
  
  FilePath := ParamStr(1);
  
  if ParamCount = 2 then
    Cores := StrToInt(ParamStr(2));
  
  SetLength(Threads, Cores);
  SetLength(Data, Cores);
  
  for I := 0 to High(Data) do
  begin
    with Data[I] do
    begin
      FBuffer := '';
      FTotalEmployees := 0;
      FTotalSalary := 0;
      FMinSalary := 0;
      FMaxSalary := 0;
      FMinNames := TFPList.Create;
      FMaxNames := TFPList.Create;
      FAreas := TFPHashList.Create;
      FSurnames := TFPHashList.Create;
    end;
  end;
  
  FileStream := TFileStream.Create(FilePath, fmOpenRead or fmShareDenyWrite);
  
  for I := 0 to High(Data) do
  begin
    if I = High(Data) then //if its the last buffer, read the remains
      BufferSize := FileStream.Size - FileStream.Position
    else
      BufferSize := Ceil(FileStream.Size / Cores);
    
    SetLength(Data[I].FBuffer, BufferSize);
    
    ReadSize := FileStream.Read(Data[I].FBuffer[1], BufferSize);
    
    for J := ReadSize downto 1 do
    begin
      if Data[I].FBuffer[J] = '}' then Break;
      
      FileStream.Position := FileStream.Position - 1;
      
      Dec(ReadSize);
    end;
    
    SetLength(Data[I].FBuffer, ReadSize);
    
    Threads[I] := TThread.ExecuteInThread(@ThreadProc, @Data[I]);
  end;
  
  FileStream.Free;
  
  for I := 0 to High(Threads) do
  begin
    Threads[I].WaitFor;
    Threads[I].Free;
  end;
  
  //join threads results
  for I := 1 to High(Data) do
  begin
    with Data[0] do
    begin
      //global
      FTotalEmployees += Data[I].FTotalEmployees;
      FTotalSalary += Data[I].FTotalSalary;
      JoinNameList(Data[I].FMinNames, FMinNames, Data[I].FMinSalary, FMinSalary, True);
      JoinNameList(Data[I].FMaxNames, FMaxNames, Data[I].FMaxSalary, FMaxSalary, False);
      
      //areas
      for J := 0 to Data[I].FAreas.Count - 1 do
      begin
        CurrentArea := Data[I].FAreas.Items[J];
        Key := Data[I].FAreas.NameOfIndex(J);
        with GetArea(FAreas, @Key)^ do
        begin
          if CurrentArea^.FName <> nil then FName := CurrentArea^.FName;
          FTotalEmployees += CurrentArea^.FTotalEmployees;
          FTotalSalary += CurrentArea^.FTotalSalary;
          JoinNameList(CurrentArea^.FMinNames, FMinNames, CurrentArea^.FMinSalary, FMinSalary, True);
          JoinNameList(CurrentArea^.FMaxNames, FMaxNames, CurrentArea^.FMaxSalary, FMaxSalary, False);
        end;
      end;
      
      //surnames
      for J := 0 to Data[I].FSurnames.Count - 1 do
      begin
        CurrentSurname := Data[I].FSurnames.Items[J];
        Key := Data[I].FSurnames.NameOfIndex(J);
        with GetSurname(FSurnames, @Key)^ do
        begin
          FTotalEmployees += CurrentSurname^.FTotalEmployees;
          JoinNameList(CurrentSurname^.FMaxNames, FMaxNames, CurrentSurname^.FMaxSalary, FMaxSalary, False);
        end;
      end;
    end;
  end;
  
  //write results
  
  //global
  with Data[0] do
  begin
    for I := 0 to FMinNames.Count div 2 - 1 do
      WriteLn('global_min|', PShortString(FMinNames[I * 2])^, ' ', PShortString(FMinNames[I * 2 + 1])^, '|', (FMinSalary * 0.01):0:2);
    
    for I := 0 to FMaxNames.Count div 2 - 1 do
      WriteLn('global_max|', PShortString(FMaxNames[I * 2])^, ' ', PShortString(FMaxNames[I * 2 + 1])^, '|', (FMaxSalary * 0.01):0:2);
    
    WriteLn('global_avg|', ((Data[0].FTotalSalary * 0.01) / Data[0].FTotalEmployees):0:2);
  end;
  
  //areas
  for I := 0 to Data[0].FAreas.Count - 1 do
  begin
    with PArea(Data[0].FAreas.Items[I])^ do
    begin
      if FTotalEmployees > 0 then
      begin
        WriteLn('area_avg|', FName^, '|', ((FTotalSalary * 0.01) / FTotalEmployees):0:2);
        
        for J := 0 to FMinNames.Count div 2 - 1 do
          WriteLn('area_min|', FName^, '|', PShortString(FMinNames[J * 2])^, ' ', PShortString(FMinNames[J * 2 + 1])^, '|', (FMinSalary * 0.01):0:2);
        
        for J := 0 to FMaxNames.Count div 2 - 1 do
          WriteLn('area_max|', FName^, '|', PShortString(FMaxNames[J * 2])^, ' ', PShortString(FMaxNames[J * 2 + 1])^, '|', (FMaxSalary * 0.01):0:2);
        
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
        WriteLn('most_employees|', FName^, '|', FTotalEmployees);
      
      if FTotalEmployees = LeastEmployees then
        WriteLn('least_employees|', FName^, '|', FTotalEmployees);
    end;
  end;
  
  //surnames
  for I := 0 to Data[0].FSurnames.Count - 1 do
  begin
    Key := Data[0].FSurnames.NameOfIndex(I);
    with PSurname(Data[0].FSurnames.Items[I])^ do
      if FTotalEmployees > 1 then
        for J := 0 to FMaxNames.Count - 1 do
          WriteLn('last_name_max|', Key, '|', PShortString(FMaxNames[J])^, ' ', Key, '|', (Double(FMaxSalary) * Double(0.01)):0:2);
  end;

end.