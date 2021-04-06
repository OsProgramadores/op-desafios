/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   TasksQueue_Manager.hpp
 * Author: Jonathas Valeriano
 *
 * Created on 7 de Novembro de 2020, 20:58
 */

#pragma once

#include <list>

#include "WorkerThread.hpp"
#include "TasksQueue.hpp"
//#include "TimedTasksQueue.hpp"
#include "Task.hpp"

namespace TTasks
{
    class TasksQueue;
//    class TimedTasksQueue;
    class WorkerThread;
    class Task_Impl;

    class TasksQueue_Manager
    {
        std::list<WorkerThread> workers;
        TasksQueue tasksQueue;
//        TimedTasksQueue timedTasksQueue;

    public:

        TasksQueue_Manager(const uint numWorkers = 8);
        ~TasksQueue_Manager();

        uint tasksCount() const { return tasksQueue.count(); }

        Task enqueue_task(bool taskType, std::function<void(Task&&)>&& fn);
        Task enqueue_task(std::function<void(Task&&)>&& fn);

//        Task enqueue_timedTask(const std::string& key, std::function<void(Task&&)>&& fn, u64 frequence, int repeat = -1, bool allowReentrance = false);
//        Task enqueue_timedTask(bool taskType, const std::string& key, std::function<void(Task&&)>&& fn, u64 frequence, int repeat = -1, bool allowReentrance = false);

        void enqueue_task_noReturn(bool taskType, std::function<void(Task&&)>&& fn);
        void enqueue_task_noReturn(std::function<void(Task&&)>&& fn);

//        void enqueue_timedTask_noReturn(const std::string& key, std::function<void(Task&&)>&& fn, u64 frequence, int repeat = -1, bool allowReentrance = false);
//        void enqueue_timedTask_noReturn(bool taskType, const std::string& key, std::function<void(Task&&)>&& fn, u64 frequence, int repeat = -1, bool allowReentrance = false);

        void finish_all();
    };
}

