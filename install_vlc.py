import requests
import hashlib
import subprocess
import os 
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    """Downloads the text file containing the expected SHA-256 value for the VLC installer file from the 
    videolan.org website and extracts the expected SHA-256 value from it.

    Returns:
        str: Expected SHA-256 hash value of VLC installer
    """
    #Step 1
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/SHA256SUMS'
    response = requests.get(file_url)
    if response.status_code == requests.codes.ok:
        file_content = response.text
        get_expected_sha256 = file_content.split()[0]  
    return get_expected_sha256
   # Hint: See example code in lab instructions entitled "Extracting Text from a Response Message Body"
    # Hint: Use str class methods, str slicing, and/or regex to extract the expected SHA-256 value from the text 

def download_installer():
    """Downloads, but does not save, the .exe VLC installer file for 64-bit Windows.

    Returns:
        bytes: VLC installer file binary data
    """
    #Step 2
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        # Extract binary file content from response message body
        file_content = response.content
        return file_content

    # Hint: See example code in lab instructions entitled "Downloading a Binary File"
    

def installer_ok(installer_data, expected_sha256):
    """Verifies the integrity of the downloaded VLC installer file by calculating its SHA-256 hash value 
    and comparing it against the expected SHA-256 hash value. 

    Args:
        installer_data (bytes): VLC installer file binary data
        expected_sha256 (str): Expeced SHA-256 of the VLC installer

    Returns:
        bool: True if SHA-256 of VLC installer matches expected SHA-256. False if not.
    """    
    #Step 3
    sha256 = hashlib.sha256(installer_data).hexdigest()
    if sha256 == expected_sha256:
        return True
    else:
        
        return False
    
    # Hint: See example code in lab instructions entitled "Computing the Hash Value of a Response Message Body"


def save_installer(installer_data):
    """Saves the VLC installer to a local directory.

    Args:
        installer_data (bytes): VLC installer file binary data

    Returns:
        str: Full path of the saved VLC installer file
    """
    #Step 4
    installer_path = os.path.join(os.getenv('TEMP'), 'vlc_installer.exe')
    with open(installer_path, 'wb') as file:
        file.write(installer_data)
    return installer_path
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"
    

def run_installer(installer_path):
    """Silently runs the VLC installer.

    Args:
        installer_path (str): Full path of the VLC installer file
    """    
    # Step 5
    subprocess.run([installer_path, '/L=1033', '/S'])
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"
    return
    
def delete_installer(installer_path):
    # Step 6
    os.remove(installer_path)
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"
    """Deletes the VLC installer file.

    Args:
        installer_path (str): Full path of the VLC installer file
    """
    return

if __name__ == '__main__':
    main()