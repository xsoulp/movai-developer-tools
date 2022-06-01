from movai_developer_tools.utils import logger
from movai_developer_tools.utils.backup_helper import BackupHelper


class ReInstaller(BackupHelper):
    """Main class to delete metadata using the backup tool in the spawner container"""

    def __init__(self):
        """If your executor requires some initialization, use the class constructor for it"""
        logger.debug("ReInstaller Init")

    def execute(self, args):
        """Execute the re-install behaviour."""
        # Call superclass init
        super().__init__(dry_run=args.dry)
        # Execute
        self.iterative_backup_action(command=args.command, work_dir=args.dir)

    @staticmethod
    def add_expected_arguments(parser):
        """Method exposed for the handle to append our executer arguments."""
