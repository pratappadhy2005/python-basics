import asyncio
import time

async def do_async_work(task_id: int, duration: float = 2.0) -> str:
    await asyncio.sleep(duration)
    return f"Task {task_id} completed after {duration} seconds"

async def run_asyncio(tasks: int=5) -> list[str]:
    task_list = [do_async_work(task_id) for task_id in range(tasks)]
    results = await asyncio.gather(*task_list)
    return results

if __name__ == "__main__":      
    start_time = time.time()
    results = asyncio.run(run_asyncio(tasks=10))    
    end_time = time.time()
    print(results)
    print(f"Total time taken: {end_time - start_time} seconds")