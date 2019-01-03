{
  Download freepascal compiler (fpc) here https://www.freepascal.org/ or thru your distro package manager
  
  Compile with:
  fpc desafio5.pas -O4
}

program Desafio5;

{$MODE OBJFPC}{$H+}

uses
  {$ifdef unix}
  cthreads,
  cmem, // the c memory manager is on some systems much faster for multi-threading
  {$endif}
  SysUtils, Classes;

const
  BufferLength = 1024 * 128; //amount of data each thread will work out from file (in Bytes)
  VectorInitialCapacity = 1;
  VectorGrowFactor = 2;
  TableSize = 997; //a prime number choosen by profilling

type
  TSmallString = string[32];
  
  PSlot = ^TSlot;
  
  TVector = record
    FLength, FCapacity: LongInt;
    FSlots: PSlot;
  end;
  
  TEmployee = record
    FName: TSmallString; //name must come first because it is checked in variant record 'TData' using 'FName';
    FId: LongInt;
    FSurname: TSmallString;
    FSalary: Double;
    FArea: TSmallString;
  end;
  
  TArea = record
    FCode: TSmallString; //name must come first because it is checked in variant record 'TData' using 'FName';
    FName: TSmallString;
    FTotalEmployees: LongInt;
    FTotalSalary: Double;
    FMaxSalary, FMinSalary: TVector;
  end;
  
  TSurname = record
    FText: TSmallString; //name must come first because it is checked in variant record 'TData' using 'FName';
    FTotalEmployees: LongInt;
    FMaxSalary: TVector;
  end;
  
  //a varint record aka union in C family language
  TSlot = record
    case FType: LongInt of
      1: (FKey: TSmallString);
      2: (FEmployee: TEmployee);
      3: (FArea: TArea);
      4: (FSurname: TSurname);
  end;
  
  //hash table
  TTable = array[0 .. TableSize - 1] of TVector;
  
  PThreadData = ^TThreadData;
  
  TThreadData = record
    FBuffer: array[0 .. BufferLength - 1] of Char;
    FLength: LongInt;
    FTotalEmployees: LongInt;
    FTotalSalary: Double;
    FMinSalary, FMaxSalary: TVector;
    FAreas, FSurnames: TTable;
    
    FTotalAreas: LongInt;
  end;
  
function Hash(const AKey: ShortString): QWord; inline;
type
  {a variant record (like an union in C language)
  is used to ease individual byte manipulation}
  TNumber = record
    case FType: Byte of
      0:
        (FData: QWord);
      1:
        (FBytes: record
          F1, F2, F3, F4, F5, F6, F7, F8: Byte;
        end)
  end;
var
  Number: TNumber;
begin
  Number.FData := 0;
  if Length(AKey) >= 1 then Number.FBytes.F1 := Byte(AKey[1]); //Pascal ShortStrings starts at 1
  if Length(AKey) >= 2 then Number.FBytes.F2 := Byte(AKey[2]);
  if Length(AKey) >= 3 then Number.FBytes.F3 := Byte(AKey[3]);
  if Length(AKey) >= 4 then Number.FBytes.F4 := Byte(AKey[4]);
  if Length(AKey) >= 5 then Number.FBytes.F5 := Byte(AKey[5]);
  if Length(AKey) >= 6 then Number.FBytes.F6 := Byte(AKey[6]);
  if Length(AKey) >= 7 then Number.FBytes.F7 := Byte(AKey[7]);
  if Length(AKey) >= 8 then Number.FBytes.F8 := Byte(AKey[8]);
  Result := Number.FData;
end;

function AppendSlot(var AVector: TVector; ASlot: PSlot): PSlot;
begin
  with AVector do
  begin
    if FLength + 1 > FCapacity then
    begin
      if FCapacity = 0 then FCapacity := VectorInitialCapacity else FCapacity := Trunc(FCapacity * VectorGrowFactor);
      FSlots := ReallocMem(FSlots, SizeOf(TSlot) * FCapacity);
    end;
    Result := @FSlots[FLength];
    Inc(FLength);
    if ASlot <> nil then
    begin
      Result^ := ASlot^;
    end
    else
      FillChar(Result^, SizeOf(TSlot), 0);
  end;
end;

function FloatEqual(AA, AB: Double): Boolean; inline;
const
  Epsilon = 0.000001;
begin
  Result := Abs(AA - AB) < Epsilon;
end;

procedure AppendEmployee(var AVector: TVector; const AEmployee: TEmployee; AKeepMinSalary: Boolean);
var
  Slot: TSlot;
begin
  Slot.FEmployee := AEmployee;
  with AVector do
  begin
    if (FLength = 0) or FloatEqual(AEmployee.FSalary, FSlots[0].FEmployee.FSalary) then
    begin
      AppendSlot(AVector, @Slot);
    end
    else if (AKeepMinSalary and (AEmployee.FSalary < FSlots[0].FEmployee.FSalary)) or
            ((not AKeepMinSalary) and (AEmployee.FSalary > FSlots[0].FEmployee.FSalary)) then
    begin
      FLength := 0;
      AppendSlot(AVector, @Slot);
    end;
  end;
end;

function GetSlot(var ATable: TTable; const AKey: TSmallString): PSlot;
var
  I, Key: SizeInt;
begin
  Key := SizeInt(Hash(AKey) mod QWord(TableSize));
  with ATable[Key] do
  begin
    for I := 0 to FLength - 1 do
    begin
      if (Length(AKey) = Length(FSlots[I].FKey)) and CompareMem(@AKey[1], @(FSlots[I].FKey[1]), Length(AKey)) then
        Exit(@FSlots[I]);
    end;
  end;
  Result := AppendSlot(ATable[Key], nil);
  Result^.FKey := AKey;
end;

function SlotCount(const ATable: TTable): SizeInt;
var
  I: SizeInt;
begin
  Result := 0;
  for I := 0 to High(ATable) do
    Result += ATable[I].FLength;
end;

function GetSlotByIndex(const ATable: TTable; AIndex: LongInt): PSlot;
var
  I: SizeInt;
begin
  for I := 0 to High(ATable) do
  begin
    if AIndex < ATable[I].FLength then
      Exit(@(ATable[I].FSlots[AIndex]))
    else
      AIndex -= ATable[I].FLength;
  end;
  Result := nil;
end;

procedure JoinEmployeeVectors(const AVectorIn: TVector; var AVectorOut: TVector; AKeepMinSalary: Boolean);
var
  I: LongInt;
begin
  with AVectorIn do
    for I := 0 to FLength - 1 do
      AppendEmployee(AVectorOut, FSlots[I].FEmployee, AKeepMinSalary);
end;

procedure LoadJsonChunk(var JsonFile: TFileStream; ABuffer: PChar; out ALength: LongInt);
begin
  ALength := JsonFile.Read(ABuffer^, BufferLength);
  
  //rewind file until a '}' is found, reading only complete objects
  if JsonFile.Position <> JsonFile.Size then
  begin
    while ABuffer[ALength - 1] <> '}' do
    begin
      Dec(ALength);
      JsonFile.Position := JsonFile.Position - 1;
    end;
  end;
end;

procedure GetString(ABuffer: PChar; var AIndex: LongInt; ALenght: LongInt; out AString: TSmallString); inline;
var
  ValueBegin: LongInt;
begin
  while (AIndex < ALenght) and (ABuffer[AIndex] <> '"') do Inc(AIndex);
  Inc(AIndex);
  ValueBegin := AIndex;
  while (AIndex < ALenght) and (ABuffer[AIndex] <> '"') do Inc(AIndex);
  if (AIndex < ALenght) and (AIndex - ValueBegin > 0) then
    SetString(AString, ABuffer + ValueBegin, AIndex - ValueBegin)
  else if AIndex - ValueBegin = 0 then
    AString := '';
  Inc(AIndex);
end;

procedure GetNumber(ABuffer: PChar; var AIndex, ALenght: LongInt; out ANumber: Double); inline;
var
  ValueBegin: LongInt;
begin
  while (AIndex < ALenght) and (not (ABuffer[AIndex] in ['0'..'9', '.'])) do Inc(AIndex);
  ValueBegin := AIndex;
  while (AIndex < ALenght) and (ABuffer[AIndex] in ['0'..'9', '.']) do Inc(AIndex);
  if (AIndex < ALenght) and (AIndex - ValueBegin > 0) then
  begin
    ABuffer[AIndex] := Char(0);
    ANumber := StrToFloat(ABuffer + ValueBegin);
  end;
  Inc(AIndex);
end;

procedure GetInteger(ABuffer: PChar; var AIndex, ALenght: LongInt; out AInteger: LongInt); inline;
var
  ValueBegin: LongInt;
begin
  while (AIndex < ALenght) and (not (ABuffer[AIndex] in ['0'..'9'])) do Inc(AIndex);
  ValueBegin := AIndex;
  while (AIndex < ALenght) and (ABuffer[AIndex] in ['0'..'9']) do Inc(AIndex);
  if (AIndex < ALenght) and (AIndex - ValueBegin > 0) then
  begin
    ABuffer[AIndex] := Char(0);
    AInteger := StrToInt(ABuffer + ValueBegin);
  end;
  Inc(AIndex);
end;

procedure ParseJsonChunk(ABuffer: PChar; ALength: LongInt; var AData: TThreadData);
var
  I: LongInt;
  Employee: TEmployee;
  Area: TArea;
begin
  I := 0;
  
  Area.FName := '';
  
  while I < ALength do
  begin
    //find a property
    while (I < ALength) and (ABuffer[I] <> '"') do Inc(I);
    Inc(I);
    
    if I >= ALength then Break;
    
    //employee (starts with i of id)
    if ABuffer[I] = 'i' then
    begin
      with Employee do
      begin
        //get id
        while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
        GetInteger(ABuffer, I, ALength, FId);
        
        //get name
        while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
        GetString(ABuffer, I, ALength, FName);
        
        //get surname
        while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
        GetString(ABuffer, I, ALength, FSurname);
        
        //get salary
        while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
        GetNumber(ABuffer, I, ALength, FSalary);
        
        //get area
        while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
        GetString(ABuffer, I, ALength, FArea);
      end;
      
      //update global counters
      Inc(AData.FTotalEmployees);
      AData.FTotalSalary += Employee.FSalary;
      AppendEmployee(AData.FMinSalary, Employee, True);
      AppendEmployee(AData.FMaxSalary, Employee, False);
      
      //update areas
      with GetSlot(AData.FAreas, Employee.FArea)^.FArea do
      begin
        Inc(FTotalEmployees);
        FTotalSalary += Employee.FSalary;
        AppendEmployee(FMinSalary, Employee, True);
        AppendEmployee(FMaxSalary, Employee, False);
      end;
      
      //update surnames
      with GetSlot(AData.FSurnames, Employee.FSurname)^.FSurname do
      begin
        Inc(FTotalEmployees);
        AppendEmployee(FMaxSalary, Employee, False);
      end;
    end
    //area (starts with c of code)
    else if ABuffer[I] = 'c' then //area
    begin
      //get code
     while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
      GetString(ABuffer, I, ALength, Area.FCode);
      
      //get name
      while (I < ALength) and (ABuffer[I] <> ':') do Inc(I);
      GetString(ABuffer, I, ALength, Area.FName);
      
      //set area name
      GetSlot(AData.FAreas, Area.FCode)^.FArea.FName := Area.FName;
    end;
  end;
end;

var
  CriticalSection: TRTLCriticalSection;
  EmployeeFile: TFileStream;

procedure ThreadProc(AData: Pointer);
begin
  TThread.CurrentThread.FreeOnTerminate := False;
  
  while not TThread.CheckTerminated do
  begin
    with PThreadData(AData)^ do
    begin
      EnterCriticalSection(CriticalSection);
      if EmployeeFile.Position = EmployeeFile.Size then
        TThread.CurrentThread.Terminate;
      LoadJsonChunk(EmployeeFile, @FBuffer[0], FLength);
      LeaveCriticalSection(CriticalSection);
      
      ParseJsonChunk(@FBuffer[0], FLength, PThreadData(AData)^);
    end;
  end;
end;

var
  Threads: array of TThread;
  Data: array of TThreadData;
  I, J: LongInt;
  TotalSalary: Double = 0.0;
  TotalEmployees: LongInt = 0;
  MostEmployees: LongInt = 0;
  LeastEmployees: LongInt = High(LongInt);
  MinSalary, MaxSalary: TVector;
  Areas, Surnames: TTable;
  
begin
  
  if ParamCount <> 1 then
  begin
    WriteLn('Usage: ', ParamStr(0), ' <input file>');
    Halt;
  end;
  
  FormatSettings.DecimalSeparator := '.';
  
  FillChar(MinSalary, SizeOf(MinSalary), 0);
  FillChar(MaxSalary, SizeOf(MaxSalary), 0);
  FillChar(Areas, SizeOf(Areas), 0);
  FillChar(Surnames, SizeOf(Surnames), 0);
  
  SetLength(Threads, TThread.ProcessorCount);
  SetLength(Data, TThread.ProcessorCount);
  
  InitCriticalSection(CriticalSection);
  
  EmployeeFile := TFileStream.Create(ParamStr(1), fmOpenRead);
  
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
  for I := 0 to High(Data) do
  begin
    //global
    TotalEmployees += Data[I].FTotalEmployees;
    TotalSalary += Data[I].FTotalSalary;
    
    JoinEmployeeVectors(Data[I].FMinSalary, MinSalary, True);
    JoinEmployeeVectors(Data[I].FMaxSalary, MaxSalary, False);
    
    //areas
    for J := 0 to SlotCount(Data[I].FAreas) - 1 do
    begin
      with GetSlotByIndex(Data[I].FAreas, J)^ do
      begin
        with GetSlot(Areas, FArea.FCode)^.FArea do
        begin
          if Length(FArea.FName) <> 0 then FName := FArea.FName;
          FTotalEmployees += FArea.FTotalEmployees;
          FTotalSalary += FArea.FTotalSalary;
          JoinEmployeeVectors(FArea.FMinSalary, FMinSalary, True);
          JoinEmployeeVectors(FArea.FMaxSalary, FMaxSalary, False);
        end;
      end;
    end;
    
    //surnames
    for J := 0 to SlotCount(Data[I].FSurnames) - 1 do
    begin
      with GetSlotByIndex(Data[I].FSurnames, J)^ do
      begin
        with GetSlot(Surnames, FSurname.FText)^.FSurname do
        begin
          FTotalEmployees += FSurname.FTotalEmployees;
          JoinEmployeeVectors(FSurname.FMaxSalary, FMaxSalary, False);
        end;
      end;
    end;
  end;
  
  //print results
  
  //global
  for I := 0 to MinSalary.FLength - 1 do
  begin
    with MinSalary.FSlots[I].FEmployee do
      WriteLn('global_min|', FName, ' ', FSurname, '|', FSalary:0:2);
  end;
  
  for I := 0 to MaxSalary.FLength - 1 do
  begin
    with MaxSalary.FSlots[I].FEmployee do
      WriteLn('global_max|', FName, ' ', FSurname, '|', FSalary:0:2);
  end;
  
  WriteLn('global_avg|', (TotalSalary / TotalEmployees):0:2);
  
  //areas
  for I := 0 to SlotCount(Areas) - 1 do
  begin
    with GetSlotByIndex(Areas, I)^.FArea do
    begin
      for J := 0 to FMaxSalary.FLength - 1 do
        with FMaxSalary.FSlots[J] do
          WriteLn('area_max|', FName, '|', FEmployee.FName, ' ', FEmployee.FSurname, '|', FEmployee.FSalary:0:2);
      
      for J := 0 to FMinSalary.FLength - 1 do
        with FMinSalary.FSlots[J] do
          WriteLn('area_min|', FName, '|', FEmployee.FName, ' ', FEmployee.FSurname, '|', FEmployee.FSalary:0:2);
      
      if FTotalEmployees > 0 then
        WriteLn('area_avg|', FName, '|', (FTotalSalary / FTotalEmployees):0:2);
      
      if FTotalEmployees > MostEmployees then
        MostEmployees := FTotalEmployees;
      
      if (FTotalEmployees > 0) and (FTotalEmployees < LeastEmployees) then
        LeastEmployees := FTotalEmployees;
    end;
  end;
  
  for I := 0 to SlotCount(Areas) - 1 do
  begin
    with GetSlotByIndex(Areas, I)^.FArea do
    begin
      if FTotalEmployees = MostEmployees then
        WriteLn('most_employees|', FName, '|', FTotalEmployees);
      
      if FTotalEmployees = LeastEmployees then
        WriteLn('least_employees|', FName, '|', FTotalEmployees);
    end;
  end;

  //surnames
  for I := 0 to SlotCount(Surnames) - 1 do
  begin
    with GetSlotByIndex(Surnames, I)^.FSurname do
      if FTotalEmployees > 1 then
        for J := 0 to FMaxSalary.FLength - 1 do
          with FMaxSalary.FSlots[J] do
            WriteLn('last_name_max|', FText, '|', FEmployee.FName, ' ', FEmployee.FSurname, '|', FEmployee.FSalary:0:2);
  end;
end.