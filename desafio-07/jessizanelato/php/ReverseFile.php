<?php

final class ReverseFile {

    private const BUFFER_SIZE = 1024 * 1024;

    private $filePath;

    public function __construct(String $path) {
        $this->filePath = $path;
    }

    public function execute() {
        $reversedFile = $this->createReversedFile();
        $this->printFile($reversedFile);
    }

    private function createReversedFile() {
        $fileName = explode('.', $this->filePath);
        $reversedName = $fileName[0] . "_r.txt";

        if(file_exists($reversedName)) {
            unlink($reversedName);
        }

        $command = "tac $this->filePath > $reversedName";
        passthru($command);

        return $reversedName;
    }

    private function printFile($path) {
        $handle = fopen($path, 'r');
        
        while (!feof($handle)) {
            $buffer = fread($handle, self::BUFFER_SIZE);
            echo $buffer;
        }
        fclose($handle);
        unlink($path);
    }

}