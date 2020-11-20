<?php

namespace Src\Business;

/**
 * Author: David Ribeiro
 * Interface Calculate
 * @package Src\Business
 */
interface Calculate
{
    /**
     * @return mixed
     */
    public function max();

    /**
     * @return mixed
     */
    public function min();

    /**
     * @return mixed
     */
    public function average();
}