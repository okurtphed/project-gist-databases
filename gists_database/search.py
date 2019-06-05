from .models import Gist

def search_gists(db_connection, **kwargs):
    
    if 'github_id' in kwargs:
        
	    query = "SELECT * FROM gists WHERE github_id = :github_id"
        
    elif 'created_at' in kwargs:
        
	    query = "SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)"
    else:
        query = "SELECT * FROM gists"
    
    #should be better way of writing query?
	
    result = []
    cursor  = db_connection.cursor()
    cursor.execute(query, kwargs)
    for row in cursor:
        result.append(Gist(row))
    return result
	
