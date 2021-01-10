/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <iostream>

#include "TasksQueue.hpp"
#include "Task.hpp"

namespace TTasks
{
    Task_Impl* TasksQueue::push_back(Task_Impl* jobFn)
    {
        std::lock_guard<std::mutex> guard(lk);
//        tasks_list.emplace_back( Fn_Wrapper{std::move(jobFn)} );
        jobFn->tasks_queue = this;
        tasks_list.emplace_back( jobFn );
        counter.fetch_add(1, std::memory_order_acq_rel);

        return jobFn;
    }

    Task_Impl* TasksQueue::try_push_back(Task_Impl* jobFn)
    {
        std::lock_guard<std::mutex> guard(lk);
//        tasks_list.emplace_back( Fn_Wrapper{std::move(jobFn)} );
        jobFn->tasks_queue = this;
        tasks_list.emplace_back( jobFn );
        counter.fetch_add(1, std::memory_order_seq_cst);

        return jobFn;
    }

    Task_Impl* TasksQueue::pop_front()
    {
        if(counter.load(std::memory_order_relaxed) == 0){ return nullptr; }

        std::lock_guard<std::mutex> guard(lk);

        if(tasks_list.empty()){ return nullptr; }

//        Fn_Wrapper fnJob = std::move( tasks_list.front() );
        Task_Impl *fnJob = tasks_list.front();
        tasks_to_delete.push_back(fnJob);
        tasks_list.pop_front();
        counter.fetch_sub(1, std::memory_order_seq_cst);

        return fnJob;
    }

    Task_Impl* TasksQueue::try_pop_smallTask()
    {
        if(counter.load(std::memory_order_relaxed) == 0){ return nullptr; }

        std::lock_guard<std::mutex> guard(lk);

        if(tasks_list.empty()){ return nullptr; }

        Task_Impl *fnJob = nullptr;

        auto it = tasks_list.begin();
        while(it != tasks_list.end())
        {
            if((*it)->m_type == SMALL_TASK)
            {
                fnJob = *it;

                int expects{0};
                if(!fnJob->m_status.compare_exchange_strong(expects, 1, std::memory_order_release, std::memory_order_relaxed))
                {
                    auto oldIt = it++;

                    tasks_list.erase(oldIt);
                    tasks_to_delete.push_back(fnJob);
                    counter.fetch_sub(1, std::memory_order_seq_cst);

                    if(tasks_list.empty()){ return nullptr; }

                    continue;
                }
                else
                {
                    tasks_list.erase(it);
                    tasks_to_delete.push_back(fnJob);
                    counter.fetch_sub(1, std::memory_order_seq_cst);

                    return fnJob;
                }
            }

            ++it;
        }

        return nullptr;
    }

    Task_Impl* TasksQueue::try_pop_front()
    {
        if(counter.load(std::memory_order_relaxed) == 0){ return nullptr; }

        std::lock_guard<std::mutex> guard(lk);

        if(tasks_list.empty()){ return nullptr; }

//        Fn_Wrapper fnJob = std::move( tasks_list.front() );
        Task_Impl *fnJob = tasks_list.front();

        int expects{0};
        while(!fnJob->m_status.compare_exchange_weak(expects, 1, std::memory_order_release, std::memory_order_relaxed))
        {
            tasks_list.pop_front();
            tasks_to_delete.push_back(fnJob);
            counter.fetch_sub(1, std::memory_order_seq_cst);

            if(tasks_list.empty()){ return nullptr; }

            fnJob = tasks_list.front();
            expects = 0;
        }

        tasks_list.pop_front();
        tasks_to_delete.push_back(fnJob);
        counter.fetch_sub(1, std::memory_order_seq_cst);

        return fnJob;
    }
}