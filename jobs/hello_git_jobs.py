from nautobot.apps.jobs import Job

name = "Git Jobs"

class HelloGitJobs(Job):

    class Meta: 
        name = "Hello Jobs from Git Repo"
        description = "Jobs synced from git"

    def run(self):
        self.logger.debug("This is from the Git repo.")