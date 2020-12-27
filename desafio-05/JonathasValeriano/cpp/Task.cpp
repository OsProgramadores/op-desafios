/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <deque>
#include <atomic>
#include <thread>
#include <cstdlib>
#include <iostream>
#include <vector>

#include "Task.hpp"
#include "TasksQueue.hpp"
#include "WorkerThread.hpp"

namespace TTasks
{
    Task_Impl::Task_Impl(std::function<void(Task&&)>&& fn, bool smallTask)
    : fn_task{std::move(fn)}, m_type{smallTask}, m_status{0}
    {
        
    }
    
    u64 Task_Impl::get_WorkerThread_uid() const
    {
        if(worker_thread){ return worker_thread->uid(); }
        
        return 0;
    }
    
    void Task_Impl::run()
    {
        fn_task( Task{this, true} );
    }
    
    void Task_Impl::co_join()
    {
        for(Task_Impl *t: sub_tasks)
        {   
            int expects{0};
            if(t->m_status.compare_exchange_strong(expects, 1, std::memory_order_release, std::memory_order_relaxed))
            {
                t->worker_thread = worker_thread;
                t->run();
            }
        }
    }
    
    void Task_Impl::stop()
    {
        const int s = m_status.load(std::memory_order_relaxed);
        if(s == 2)
        { 
            if(root){ root->success(); }
        }
        else if(s == -1)
        {  
            if(root){ root->abort(); }
        }
    }
    
    void Task_Impl::success()
    {
        for(Task_Impl *t: sub_tasks)
        {
            t->success();
        }
        
        m_status.store(2, std::memory_order_release);
    }
    
    void Task_Impl::abort()
    {
        for(Task_Impl *t: sub_tasks)
        {
            t->abort();
        }
        
        m_status.store(-1, std::memory_order_release);
    }
    
    void Task_Impl::wait()
    {
        if(!sub_tasks.empty())
        {
            while(1)
            {
                bool must_return{true};
                
                for(Task_Impl *t: sub_tasks)
                {
                    if(!t->must_stop()){ must_return = false; break; }
                }
                
                if(must_return){ return; }
                
                std::this_thread::sleep_for(std::chrono::microseconds{2});
            }
        }
    }
    
    void Task_Impl::co_wait()
    {
        if(!sub_tasks.empty())
        {
            while(1)
            {
                bool must_return{true};
                
                for(Task_Impl *t: sub_tasks)
                {
                    if(!t->must_stop()){ must_return = false; break; }
                }
                
                if(must_return){ return; }
                
                if(Task_Impl* t = tasks_queue->try_pop_smallTask())
                {
                    t->worker_thread = worker_thread;
                    t->run();
                }
                
                std::this_thread::sleep_for(std::chrono::microseconds{2});
            }
        }
    }
    
    void Task_Impl::co_wait(u32 time_in_us)
    {
        const auto beg = std::chrono::high_resolution_clock::now();
        std::chrono::time_point<std::chrono::high_resolution_clock> end{};
        std::chrono::duration<double, std::micro> diff{};
        
        u32 sleep_time = time_in_us / 4;
        sleep_time = (sleep_time > 0? sleep_time: time_in_us);
        
        while(1)
        {
            end = std::chrono::high_resolution_clock::now();
            diff = end-beg;
            
            if(diff.count() < time_in_us)
            {
                if(Task_Impl* t = tasks_queue->try_pop_smallTask())
                {
//                    std::cout << "on Task_Impl::co_wait(u32 time_in_us) --- t->run()" << std::endl;
                    t->run();
                }
//                else
//                {
//                    std::this_thread::sleep_for(std::chrono::microseconds{sleep_time});
//                    continue;
//                }
            }
            else { return; }
        }
    }
    
    void Task_Impl::co_wait(Task_Impl& task)
    {
        while(1)
        {
            if(task.must_stop()){ return; }
            
            if(Task_Impl* t = tasks_queue->try_pop_smallTask())
            {
                t->run();
            }
            
//            std::cout << "in co_wait -- " << task.m_status.load() << std::endl;
            
            std::this_thread::sleep_for(std::chrono::microseconds{2});
        }
    }
    
    void Task_Impl::wait(Task_Impl& t)
    {
        while(1)
        {
            if(t.must_stop()){ return; }
            
            std::this_thread::sleep_for(std::chrono::microseconds{2});
        }
    }
    
    int Task_Impl::status() const
    {
        return m_status.load();
    }

    bool Task_Impl::must_stop() const
    {    
        if(!sub_tasks.empty())
        {
            for(Task_Impl *t: sub_tasks)
            {
                if(t && !t->must_stop()){ return false; }
            }
        }

        const int s = m_status.load(std::memory_order_relaxed);
        
        return (s == -1 || s == 2);
    }
    
    void Task_Impl::set_success()
    {
        m_status.store(2, std::memory_order_release);
    }
    
    void Task_Impl::set_abort()
    {
        m_status.store(-1, std::memory_order_release);
    }
    
    Task_Impl* Task_Impl::enqueue_sub_task(bool task_type, std::function<void(Task&&)>&& fn)
    {
//        if(m_type == LONG_TASK)
        {
            Task_Impl *t = new Task_Impl{ std::move(fn), task_type };
            t->parent = this;
            t->root = (root? root: this);
            t->tasks_queue = tasks_queue;

            tasks_queue->push_back( t );
            sub_tasks.push_back( t );

            return t;
        }
        
        std::cerr << "\n\nSIGABRT: Program execution aborted hence Task::enqueue_sub_task call from SMALL_TASK type is not permited. To enqueue_sub_tasks you need a LONG_TASK.\n\n";
        std::abort();
    }
    
    Task_Impl* Task_Impl::enqueue_sub_task(std::function<void(Task&&)>&& fn)
    {
//        if(m_type == LONG_TASK)
        {
            Task_Impl *t = new Task_Impl{ std::move(fn) };
            t->parent = this;
            t->root = (root? root: this);
            t->tasks_queue = tasks_queue;

            tasks_queue->push_back( t );
            sub_tasks.push_back( t );

            return t;
        }
        
        
        std::cerr << "\n\nSIGABRT: Program execution aborted hence Task::enqueue_sub_task call from SMALL_TASK type is not permited. To enqueue_sub_tasks you need a LONG_TASK.\n\n";
        std::abort();
    }
    
    u32 Task_Impl::sub_tasks_count() const
    {
        return sub_tasks.size();
    }
    
    
    /*
     *  ----------------------------------
     *       CurTask implementation
     *  ----------------------------------
     */
    
    Task::Task(Task&& o) : m_task{o.m_task}, m_flag{o.m_flag} { o.m_task = nullptr; o.m_flag = false; }

    Task::~Task()
    {
        if(m_flag && m_task && m_task->status() != -1)
        { 
            m_task->set_success(); 
//            m_task->fn_task = nullptr;
        }
        
    }
    
    Task& Task::operator= (Task&& o)
    {
        m_task = o.m_task;
        m_flag = o.m_flag;
        
        o.m_flag = false;
        o.m_task = nullptr;
        
        return *this;
    }
    
    Task::operator bool () const { return m_task != nullptr; }
        
    u64 Task::get_WorkerThread_uid() const
    {
        return m_task->get_WorkerThread_uid();
    }

    void Task::run()
    {
        m_task->run();
    }
    
    void Task::stop()
    {
        m_task->stop();
    }
    
    void Task::co_join()
    {
        m_task->co_join();
    }
    
    void Task::co_wait()
    {
        m_task->co_wait();
    }
    
    void Task::co_wait(u32 time_in_us)
    {
        m_task->co_wait(time_in_us);
    }
    
    void Task::co_wait(Task& t)
    {
        m_task->co_wait( *(t.m_task) );
    }
    
    void Task::wait()
    {
        m_task->wait();
    }
    
    void Task::wait(Task& t)
    {
        m_task->wait( *(t.m_task) );
    }
    
    int Task::status() const { return m_task->status(); }

    bool Task::can_stop() const { return m_task->must_stop(); }
    void Task::set_success() { m_task->set_success(); }
    void Task::set_abort(){ m_task->set_abort(); }
    u32 Task::sub_tasks_count() const { return m_task->sub_tasks_count(); }

    bool Task::self_run()
    {
        int expects{0};
        if(m_task->m_status.compare_exchange_strong(expects, 1, std::memory_order_release, std::memory_order_relaxed))
        {
            m_task->run();
            return true;
        }
        
        return false;
    }
    
    Task Task::enqueue_sub_task(std::function<void(Task&&)>&& fn)
    {
        return m_task->enqueue_sub_task( std::move(fn) );
    }
    
    Task Task::enqueue_sub_task(bool task_type, std::function<void(Task&&)>&& fn)
    {
        return m_task->enqueue_sub_task( task_type, std::move(fn) );
    }
    
    void Task::enqueue_sub_task_noReturn(std::function<void(Task&&)>&& fn)
    {
        m_task->enqueue_sub_task( std::move(fn) );
    }
    
    void Task::enqueue_sub_task_noReturn(bool task_type, std::function<void(Task&&)>&& fn)
    {
        m_task->enqueue_sub_task( task_type, std::move(fn) );
    }
}