/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <vector>

#include "WorkerThread.hpp"
#include "TasksQueue.hpp"

namespace TTasks
{
    void WorkerThread::add_job(Task_Impl* jobFn)
    {
        active_task = jobFn;
        active_task->worker_thread = this;
        m_status.store(STATUS::HAVE_JOB, std::memory_order_release);
    }

    void WorkerThread::loop(TasksQueue& tasksQueue)
    {
        jobsQueuePtr = &tasksQueue;
        u32 idle_count{0};

        while(1)
        {
            if(m_status.load(std::memory_order_relaxed) == STATUS::FINISHED){ return; }

            if(tasksQueue.count() > (u32)0 && may_work() == STATUS::IDLE)
            {
                if(Task_Impl* fn = tasksQueue.try_pop_front())
                {
                    add_job( fn );
                }
                else { m_status.store(STATUS::IDLE, std::memory_order_release); }
            }

            STATUS s{STATUS::HAVE_JOB};
            if(!m_status.compare_exchange_strong(s, STATUS::WORKING, std::memory_order_release, std::memory_order_relaxed))
            {
                if(m_status.load(std::memory_order_relaxed) == STATUS::FINISHED){ return; }

                if(++idle_count >= 500)
                {
                    idle_count = 0;
                    std::this_thread::sleep_for(std::chrono::microseconds{1});
                }
            }

            if(active_task && *active_task)
            {
                active_task->run();

                active_task = nullptr;

                m_status.store(STATUS::IDLE, std::memory_order_release);
            }
        }
//        std::cout << "thread: " << std::this_thread::get_id() << " FINISHED.\n";
        active_task = nullptr;
    }
}