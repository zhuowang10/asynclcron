import asyncio
from datetime import datetime
from asynclcron.lcron import LightweightCron


async def run_job(text, context):
    print(f"[{datetime.now()}] run_job: {text}, context.cron_job: {context['cron_job']}")

async def run():
    print(f"[{datetime.now()}] start")
    schedule = LightweightCron(log_next_run_datetime=False)

    # optionally add/remove cron jobs before schedule run
    # ...

    # run schedule
    schedule_task = asyncio.create_task(schedule.run())
    await asyncio.sleep(1)

    # add a job
    job1 = schedule.add(run_job, "0 0 * * * ", kwargs={"text": "I'm job1"}, name="job1")
    # doing something
    await asyncio.sleep(0.3)
    # then add 2 more jobs
    job2 = schedule.add(run_job, "* * * * * */7", kwargs={"text": "I'm job2"}, name="job2")
    job3 = schedule.add(run_job, "* * * * * */3", kwargs={"text": "I'm job3"}, name="job3")

    # let jobs to run
    await asyncio.sleep(20)

    # remove job1
    schedule.remove(job2.job_id)

    # remaining jobs are running
    await asyncio.sleep(10)

    # end schedule
    schedule_task.cancel()
    # return_exceptions=True may hide should-be-handled exceptions other than cancel
    asyncio.gather(schedule_task, return_exceptions=True)

    print(f"[{datetime.now()}] end")

if __name__ == "__main__":
    asyncio.run(run())
