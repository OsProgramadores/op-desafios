/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include "TimedTasksQueue.hpp"
#include "TasksQueue_Manager.hpp"

#include <chrono>
#include <thread>

namespace TTasks
{
    TimedTasksQueue::TimedTask::TimedTask(Task_Impl* task, const std::string& key, u64 frequence, int repeat)
    : fn_task{ task }, key{key}, frequence{frequence}, repeat{repeat}
    {

    }

    TimedTasksQueue::TimedTask::TimedTask(Task_Impl* task, const std::string& key, bool allowReentrance, u64 frequence, int repeat)
    : fn_task{ task }, key{key}, frequence{frequence}, repeat{repeat}, allowReentrance{allowReentrance}
    {

    }

    TimedTasksQueue::TimedTask::~TimedTask()
    {
        delete fn_task;
    }
    
    void TimedTasksQueue::lock()
    {
        bool expects{false};
        while(!lk.compare_exchange_weak(expects, true, std::memory_order_release, std::memory_order_relaxed))
        {
            expects = false;
        }
    }

    void TimedTasksQueue::unlock()
    {
        lk.store(false, std::memory_order_release);
    }
    
    void TimedTasksQueue::queueLoop()
    {
        std::chrono::high_resolution_clock::time_point timeNow = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> diff;

        u64 maxSleepTime{500}; //milliseconds
        
        while(1)
        {
            timeNow = std::chrono::high_resolution_clock::now();
            
            lock();
            {
                auto iter = jobs_list.begin();
                while(iter != jobs_list.end())
                {
                    auto current_iter = iter++;
                    if(current_iter->repeat != 0)
                    {
                        diff = timeNow - current_iter->timer;
                        if(diff.count() >= current_iter->frequence)
                        {
                            current_iter->timer = timeNow;
//                            std::cout << "diff.count = " << diff.count() 
//                                      << " ---- time frequence = " << current_iter->frequency << std::endl;
                            auto &job = *current_iter;
                            tasksQueue_manager->enqueue_task(job.fn_task->m_type, [&job = *current_iter](Task&&)
                            { 
//                                std::cout << job.key << " -- begin...\n" << std::endl;
                                if(job.reentrance.load(std::memory_order_release) < 0)
                                { 
                                    return; 
                                }
                                else if(job.allowReentrance)
                                {
                                    job.reentrance.fetch_add(1, std::memory_order_relaxed);
                                    job.fn_task->run();
                                    job.reentrance.fetch_sub(1, std::memory_order_relaxed);
                                }
                                else
                                {
                                    if(job.reentrance.exchange(1, std::memory_order_acquire) == 0)
                                    {
                                        job.fn_task->run();
                                        job.reentrance.store(0, std::memory_order_release);
                                    }
                                }
//                                std::cout << job.key << " -- end.\n" << std::endl;    
                            });

                            if(current_iter->repeat > 0)
                            {
                                current_iter->repeat--;
                            }
                        }
                    }
                    else
                    {
                        if(current_iter->reentrance.load(std::memory_order_relaxed) == 0)
                        {
                            jobs_list.erase(current_iter);
                        }
                    }
                }
            }
            unlock();
            
            if(m_stop.load(std::memory_order_relaxed) == true){ return; }
            
            std::this_thread::sleep_for(std::chrono::milliseconds{maxSleepTime});
        }
    }
    
    Task_Impl* TimedTasksQueue::push_back(const std::string& key, Task_Impl* jobFn, u64 frequence, int repeat)
    {
        lock();
        
        if(frequence > longestTimerFrequence){ longestTimerFrequence = frequence; }
        if(frequence < shortestTimerFrequence){ shortestTimerFrequence = frequence; }
        
        jobs_list.emplace_back( jobFn, key, frequence, repeat );
        
        if(counter.fetch_add(1, std::memory_order_seq_cst) == 0)
        {
            m_stop.exchange(false, std::memory_order_release);
            tasksQueue_manager->enqueue_task(LONG_TASK, [this](Task&& task){ queueLoop(); });
        }
        
        unlock();
        
        return jobFn;
    }

    bool TimedTasksQueue::remove(const std::string& key)
    {
        lock();
        auto iter = jobs_list.begin();
        while(iter != jobs_list.end())
        {
            auto current_iter = iter++;
            if(current_iter->key == key)
            { 
                jobs_list.erase(current_iter); 
                counter.fetch_sub(1, std::memory_order_seq_cst);
                unlock();
                return true;
            }
        }
        unlock();
        
        return false;
    }
}