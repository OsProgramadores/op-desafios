/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   TimedJobsQueue.hpp
 * Author: Jonathas Valeriano
 *
 * Created on 7 de Novembro de 2020, 20:55
 */

#pragma once

#include <string>
#include <chrono>
#include <atomic>
#include <list>
#include <vector>

//#include "Task.hpp"

namespace TTasks
{
    using u64 = std::uint64_t;
    using u32 = std::uint32_t;
    
    class Task_Impl;
    class TasksQueue_Manager;
    
    class TimedTasksQueue
    {
        struct TimedTask
        {
            Task_Impl *fn_task{nullptr};
            const std::string key;
            u64 frequence{500}; //in milliseconds
            int repeat{-1}; //-1 = forever
            std::chrono::high_resolution_clock::time_point timer = std::chrono::high_resolution_clock::now();
            std::atomic<int> reentrance{0};
            const bool allowReentrance{false};
            
            TimedTask(Task_Impl* task, const std::string& key, u64 frequence = 500, int repeat = -1);
            
            TimedTask(Task_Impl* task, const std::string& key, bool allowReentrance, u64 frequence = 500, int repeat = -1);
            
            ~TimedTask();
        };
        
        std::list< TimedTask > jobs_list;
        u64 longestTimerFrequence{0};
        u64 shortestTimerFrequence{std::numeric_limits<u64>::max()};
        std::atomic<bool> m_stop{false};
        std::atomic<bool> lk{false};
        std::atomic<uint> counter{0};
        TasksQueue_Manager *tasksQueue_manager{nullptr};
        
        void lock();
        void unlock();
        
        void queueLoop();
        
        TimedTasksQueue() = delete;
        
    public:
        
        TimedTasksQueue(TasksQueue_Manager* events_queue) : tasksQueue_manager{events_queue} {}
        
        Task_Impl* push_back(const std::string& key, Task_Impl* jobFn, u64 frequence, int repeat = -1);
        bool remove(const std::string& key);
        
        void stop(){ m_stop.store(true); }
        bool isRunning() const { return !m_stop.load(std::memory_order_relaxed); }
    };
}

