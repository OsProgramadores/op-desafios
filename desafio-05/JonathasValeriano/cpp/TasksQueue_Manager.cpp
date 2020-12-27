/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <iostream>
#include <vector>

#include "Task.hpp"
#include "WorkerThread.hpp"
#include "TasksQueue.hpp"
#include "TimedTasksQueue.hpp"
#include "TasksQueue_Manager.hpp"

namespace TTasks
{
    TasksQueue_Manager::TasksQueue_Manager(const uint numWorkers) : timedTasksQueue{this}
    {
        for(uint i=1; i <= numWorkers; i++)
        {
            workers.emplace_back(tasksQueue, i);
        }
    }
    
    TasksQueue_Manager::~TasksQueue_Manager()
    {
        finish_all();
    }

    Task TasksQueue_Manager::enqueue_task(std::function<void(Task&&)>&& fn)
    {
        return tasksQueue.push_back( new Task_Impl{ std::move(fn) } );
    }
    
    Task TasksQueue_Manager::enqueue_task(bool task_type, std::function<void(Task&&)>&& fn)
    {
        return tasksQueue.push_back( new Task_Impl{ std::move(fn), task_type } );
    }

    Task TasksQueue_Manager::enqueue_timedTask(const std::string& key, std::function<void(Task&&)>&& task, u64 frequence, int repeat, bool allowReentrance)
    {
        return timedTasksQueue.push_back( key, new Task_Impl{ std::move(task) }, frequence, repeat );
    }

    Task TasksQueue_Manager::enqueue_timedTask(bool taskType, const std::string& key, std::function<void(Task&&)>&& task, u64 frequence, int repeat, bool allowReentrance)
    {
        return timedTasksQueue.push_back( key, new Task_Impl{ std::move(task), taskType }, frequence, repeat );
    }
    
    void TasksQueue_Manager::enqueue_task_noReturn(std::function<void(Task&&)>&& fn)
    {
        tasksQueue.push_back( new Task_Impl{ std::move(fn) } );
    }
    
    void TasksQueue_Manager::enqueue_task_noReturn(bool task_type, std::function<void(Task&&)>&& fn)
    {
        tasksQueue.push_back( new Task_Impl{ std::move(fn), task_type } );
    }
    
    void TasksQueue_Manager::enqueue_timedTask_noReturn(const std::string& key, std::function<void(Task&&)>&& task, u64 frequence, int repeat, bool allowReentrance)
    {
        timedTasksQueue.push_back( key, new Task_Impl{ std::move(task) }, frequence, repeat );
    }
    
    void TasksQueue_Manager::enqueue_timedTask_noReturn(bool taskType, const std::string& key, std::function<void(Task&&)>&& task, u64 frequence, int repeat, bool allowReentrance)
    {
        timedTasksQueue.push_back( key, new Task_Impl{ std::move(task), taskType }, frequence, repeat );
    }

    void TasksQueue_Manager::finish_all()
    {
        if(timedTasksQueue.isRunning())
        {
            timedTasksQueue.stop();
        }
        
        while(tasksQueue.count()){ std::this_thread::sleep_for(std::chrono::milliseconds{10}); }
        
        for(WorkerThread &w: workers){ w.finish(); }
    }
}