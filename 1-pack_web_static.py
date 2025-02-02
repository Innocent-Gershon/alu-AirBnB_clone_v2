#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repository.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Compresses the contents of the 'web_static' folder into a .tgz archive.

    - The archive will be stored inside the 'versions' folder.
    - If the 'versions' folder does not exist, it is created.
    - The archive name format is: web_static_<year><month><day><hour><minute><second>.tgz
    - Returns the path of the generated archive if successful.
    - Returns None if the archive creation fails.

    Returns:
        str: The path of the created archive if successful, else None.
    """

    # Ensure the 'versions' directory exists
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate timestamp for unique archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Create the archive using tar
    command = f"tar -cvzf {archive_name} web_static"

    # Execute the command
    result = local(command)

    # Return archive path if successful, else None
    if result.succeeded:
        return archive_name
    else:
        return None

