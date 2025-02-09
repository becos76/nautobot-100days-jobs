from nautobot.apps.jobs import register_jobs
from .hello_git_jobs import HelloGitJobs

register_jobs(HelloGitJobs)
