from __future__ import print_function
import httplib2
import os
import io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaIoBaseDownload

drive_service = discovery.build('drive', 'v3')
file_id = '0B7ON4Bg4H1ZTdVQ5YVZKeEFBOFE'
request = drive_service.files().export_media(fileId=file_id,
											mimeType='text/html')
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
	status, done = downloader.next_chunk()
	print ("Download %d%%." % int(status.progress() * 100))
