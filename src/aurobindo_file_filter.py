import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    
    source_folder = 'aurobindo_admin/in/'
    
    archive_folder = 'aurobindo_admin/in_archive/'
    
    destination_bucket = 'cflo-automated-ingestion'
    destination_folder = 'Inbound/'
    dest_key = ''
    copy_source = ''
    
    file_match_keywords = ['vm', 'po', 'gmo']
    
    for record in event['Records']:
        
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        file_name = key[len(source_folder):]
        name_parts = file_name.split('_')
        
        copy_source = {'Bucket': source_bucket, 'Key': key}
        
        
        
        # Check if the file is in the source folder and contains any of the keywords
        if key.startswith(source_folder) and len(name_parts) > 3 and name_parts[3] in file_match_keywords:
            # Extract the file name from the key
            file_name = key[len(source_folder):]
    
            
            # Copy the file to the destination
            destination_key = destination_folder + file_name
            
            s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
            
            # Delete the file from the source folder
            #s3.delete_object(Bucket=source_bucket, Key=key)
        
        # Move the file to archive folder
        archive_folder = "aurobindo_admin/in_archive/"
        archive_key = archive_folder + file_name
        
        s3.copy_object(CopySource=copy_source, Bucket=source_bucket, Key=archive_key)
        

    return {
        'statusCode': 200,
        'body': 'Files moved successfully!'
    }
