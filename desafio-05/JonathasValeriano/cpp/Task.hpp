/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   Task.hpp
 * Author: Jonathas Valeriano
 *
 * Created on 7 de Novembro de 2020, 18:57
 */


#pragma once

#include <functional>
#include <atomic>
#include <deque>
#include <cstdint>

namespace TTasks
{
    #define SMALL_TASK false
    #define LONG_TASK true

    using u64 = std::uint64_t;
    using u32 = std::uint32_t;

    class WorkerThread;
    class TasksQueue;
    class TimedTasksQueue;

    class Task;

    class Task_Impl
    {
        std::function<void(Task&&)> fn_task;
        std::vector<Task_Impl*> sub_tasks;
        WorkerThread *worker_thread{nullptr};
        TasksQueue *tasks_queue{nullptr};
        Task_Impl *root{nullptr};
        Task_Impl *parent{nullptr};
        std::atomic<int> m_status{-2}; //0 = Not_Running; 1 = Running; 2 = Success; -1 = Aborted; -2 = NULL_TASK;
        const bool m_type{SMALL_TASK}; //true = Normal_Task; false = Small_Task

        void success();
        void abort();

        operator bool() const { return fn_task.operator bool(); }

        friend WorkerThread;
        friend TimedTasksQueue;
        friend TasksQueue;
        friend Task;

    public:

        Task_Impl() = default;
        Task_Impl(std::function<void(Task&&)>&& fn, bool smallTask = SMALL_TASK);

        u64 get_WorkerThread_uid() const;

        void run();
        void co_join();
        void stop();
        void wait();
        void co_wait();
        void co_wait(u32 time_in_us);
        void co_wait(Task_Impl&);
        void wait(Task_Impl&);

        int status() const;

        bool must_stop() const;
        void set_success();
        void set_abort();
        u32 sub_tasks_count() const;

        Task_Impl* enqueue_sub_task(std::function<void(Task&&)>&&);
        Task_Impl* enqueue_sub_task(bool task_type, std::function<void(Task&&)>&&);
    };

    class Task
    {
        Task_Impl *m_task{nullptr};
        bool m_flag{false}; //false = don't set success

        void run();

    public:

        Task() = default;
        Task(Task_Impl *task, bool destroyFlag = false) : m_task{task}, m_flag{destroyFlag} {}
        Task(Task&& o);

        ~Task();

        Task& operator= (Task&& o);

        u64 get_WorkerThread_uid() const;

        void co_join();
        void stop();
        void wait();
        void co_wait();
        void co_wait(u32 time_in_us);
        void co_wait(Task&);
        void wait(Task&);

        int status() const;

        bool can_stop() const;
        void set_success();
        void set_abort();
        u32 sub_tasks_count() const;

        operator bool () const;

        bool self_run();

        Task enqueue_sub_task(std::function<void(Task&&)>&&);
        Task enqueue_sub_task(bool task_type, std::function<void(Task&&)>&&);

        void enqueue_sub_task_noReturn(std::function<void(Task&&)>&&);
        void enqueue_sub_task_noReturn(bool task_type, std::function<void(Task&&)>&&);
    };
}

