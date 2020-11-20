<?php

spl_autoload_register(function (string $namespace) {
    $classPath = str_replace("\\", DIRECTORY_SEPARATOR, $namespace);
    $classPath = str_replace("Src", "src", $classPath);

    require_once getcwd() .  DIRECTORY_SEPARATOR . "{$classPath}.php";
});
