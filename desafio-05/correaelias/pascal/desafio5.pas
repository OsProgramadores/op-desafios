{
  Solução do desafio 5 em Pascal por Elias Correa (Jan/2019)
  
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
  BufferLength = 1024 * 1024 * 16; //amount of data each thread will work out from file (in Bytes)
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
    FName: TSmallString; //name must come first because it is checked in variant record 'TSlot' using 'FName';
    FSurname: TSmallString;
    FSalary: Double;
    FArea: TSmallString;
  end;
  
  TArea = record
    FCode: TSmallString; //name must come first because it is checked in variant record 'TSlot' using 'FName';
    FName: TSmallString;
    FTotalEmployees: LongInt;
    FTotalSalary: Double;
    FMaxSalary, FMinSalary: TVector;
  end;
  
  TSurname = record
    FText: TSmallString; //name must come first because it is checked in variant record 'TSlot' using 'FName';
    FTotalEmployees: LongInt;
    FMaxSalary: TVector;
  end;
  
  //a varint record aka union in C family languages
  TSlot = record
    case FType: LongInt of
      1: (FKey: TSmallString);
      2: (FEmployee: TEmployee);
      3: (FArea: TArea);
      4: (FSurname: TSurname);
  end;
  
  //handmade hash table
  TTable = array[0 .. TableSize - 1] of TVector;
  
  PThreadData = ^TThreadData;
  
  TThreadData = record
    FBuffer: array[0 .. BufferLength - 1] of Char;
    FTotalEmployees: LongInt;
    FTotalSalary: Double;
    FMinSalary, FMaxSalary: TVector;
    FAreas, FSurnames: TTable;
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

procedure GetString(var ABuffer: PChar; out AString: TSmallString); inline;
var
  Start, C: PChar;
begin
  C := ABuffer;
  
  while (C^ <> #0) and (C^ <> '"') do Inc(C);
  if C^ = '"' then Inc(C); //skip '"'
  
  Start := C;
  
  while (C^ <> #0) and (C^ <> '"') do Inc(C);
  
  if (C^ = '"') and (Start^ <> '"') then
    SetString(AString, Start, C - Start)
  else //empty string
    AString := '';
  
  if C^ = '"' then Inc(C); //skip '"'
  
  ABuffer := C;
end;

procedure GetNumberFast(var ABuffer: PChar; out ANumber: Double); inline;
var
  C: PChar;
  Number: LongInt = 0;
begin
  C := ABuffer;

  while (C^ <> #0) and (not (C^ in ['0'..'9', '.'])) do Inc(C);
  
  while C^ in ['0'..'9', '.'] do
  begin
    if C^ <> '.' then
      Number := Number * 10 + (LongInt(C^) - LongInt('0'));
    Inc(C);
  end;
  ANumber := Double(Number) * Double(0.01);
  
  ABuffer := C;
end;

procedure ParseJsonChunk(ABuffer: PChar; var AData: TThreadData);
var
  C: PChar;
  Employee: TEmployee;
  Area: TArea;
begin
  Employee.FName := '';
  
  Area.FName := '';
  
  C := ABuffer;
  
  while C^ <> #0 do
  begin
    //find a property
    while (C^ <> #0) and (C^ <> '"') do Inc(C);
    if C^ = '"' then Inc(C); //skip '"'
    
    //employee (starts with i of id)
    if C^ = 'i' then
    begin
      with Employee do
      begin
        //ignore id
        while (C^ <> #0) and (C^ <> ',') do Inc(C);
        
        //get name
        while (C^ <> #0) and (C^ <> ':') do Inc(C);
        GetString(C, FName);
        
        //get surname
        while (C^ <> #0) and (C^ <> ':') do Inc(C);
        GetString(C, FSurname);
        
        //get salary
        while (C^ <> #0) and (C^ <> ':') do Inc(C);
        GetNumberFast(C, FSalary);
        
        //get area
        while (C^ <> #0) and (C^ <> ':') do Inc(C);
        GetString(C, FArea);
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
    else if C^ = 'c' then //area
    begin
      //get code
     while (C^ <> #0) and (C^ <> ':') do Inc(C);
      GetString(C, Area.FCode);
      
      //get name
      while (C^ <> #0) and (C^ <> ':') do Inc(C);
      GetString(C, Area.FName);
      
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
