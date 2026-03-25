/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   TasksQueue.hpp
 * Author: Jonathas Valeriano
 *
 * Created on 7 de Novembro de 2020, 20:51
 */

#pragma once

#include <vector>
#include <list>
#include <mutex>
#include <atomic>

namespace TTasks
{
    class Task_Impl;

    class TasksQueue
    {
        std::vector< Task_Impl* > tasks_to_delete;
        std::list< Task_Impl* > tasks_list;
        std::mutex lk;
        std::atomic<uint> counter{0};

        Task_Impl* try_pop_smallTask();

        friend Task_Impl;

    public:

        TasksQueue() = default;

        Task_Impl* push_back(Task_Impl* task);
        Task_Impl* try_push_back(Task_Impl* task);
        Task_Impl* pop_front();
        Task_Impl* try_pop_front();
        uint count() const { return counter.load(std::memory_order_seq_cst); }
    };
}

