/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   WorkerThread.hpp
 * Author: Jonathas Valeriano
 *
 * Created on 7 de Novembro de 2020, 20:36
 */

#pragma once

#include "Task.hpp"
#include <thread>
#include <string>

#include <iostream>

namespace TTasks
{
    class TasksQueue;
    class Task_Impl;

    class WorkerThread
    {
        std::thread thread_loop;
        TasksQueue *jobsQueuePtr{nullptr};
        Task_Impl *active_task{nullptr};
        const u64 m_uid;

        void loop(TasksQueue& tasksQueue);

    public:

        WorkerThread(TasksQueue& tasksQueue, u64 uid)
        : m_uid{uid}, thread_loop([this, &tasksQueue](){ this->loop(tasksQueue); }), m_status{STATUS::IDLE}
        {
            m_status = STATUS::IDLE;
        }

        u64 uid() const { return m_uid; }
    //    ~WorkerThread()
    //    {
    ////        std::cout << std::string{"WorkerThread dtr -> "};
    //
    //        STATUS s{STATUS::IDLE};
    //        while(!m_status.compare_exchange_weak(s, STATUS::FINISHED)){ s = STATUS::IDLE; }
    //
    //        if(thread_loop.joinable()){ thread_loop.join(); }
    ////        std::cout << std::string{"Done.\n"};
    //    }

        enum class STATUS
        {
            IDLE = 0,
            FINISHED,
            GOING_TO_WORK,
            HAVE_JOB,
            WORKING
        };

        void add_job(Task_Impl* jobFn);

        STATUS may_work()
        {
            STATUS s{STATUS::IDLE};
            while(!m_status.compare_exchange_weak(s, STATUS::GOING_TO_WORK, std::memory_order_release, std::memory_order_relaxed)){ return s; }

            return STATUS::IDLE;
        }

        void finish()
        {
            if(m_status.load(std::memory_order_seq_cst) != STATUS::FINISHED)
            {
                STATUS s{STATUS::IDLE};
                while(!m_status.compare_exchange_weak(s, STATUS::FINISHED)){ s = STATUS::IDLE; }

                thread_loop.join();
//                std::cout << std::string{"WorkerThread " + std::to_string(uid()) + " finished"} << std::endl;
            }
        }


        STATUS status() const { return (!active_task? m_status.load(): STATUS::WORKING); }

    protected:

        std::atomic<STATUS> m_status{STATUS::IDLE};
    };
}