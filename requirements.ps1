conda install selenium
conda install configparser

$source = 'https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip'
$filePath = './chromedriver.zip'
Invoke-WebRequest -Uri $source -OutFile $filePath

Expand-Archive -Path $filePath -DestinationPath './'

Remove-Item $filePath