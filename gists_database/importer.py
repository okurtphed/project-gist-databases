import requests

#db: db_connection 

URL_TEMPLATE = 'https://api.github.com/users/{username}/gists'

query = '''INSERT INTO gists (
	    "github_id", 
        "html_url", 
        "git_pull_url",
	    "git_push_url", 
        "commits_url",
	    "forks_url", 
        "public", 
        "created_at",
	    "updated_at", 
        "comments", 
        "comments_url"
	) VALUES (
	    :github_id, 
        :html_url, 
        :git_pull_url,
	    :git_push_url, 
        :commits_url,
	    :forks_url, 
        :public, 
        :created_at,
	    :updated_at, 
        :comments, 
        :comments_url
	);'''

def import_gists_to_database(db, username, commit=True):
    
    #url = 'https://api.github.com/users/{}/gists'.format(username = username)
    url = URL_TEMPLATE.format(username = username)
    request = requests.get(url)
    request.raise_for_status()
    gists_data = request.json()
    cursor = db.cursor()
    for gist in gists_data:
	        params = {
	            "github_id": gist['id'],
	            "html_url": gist['html_url'],
	            "git_pull_url": gist['git_pull_url'],
	            "git_push_url": gist['git_push_url'],
	            "commits_url": gist['commits_url'],
	            "forks_url": gist['forks_url'],
	            "public": gist['public'],
	            "created_at": gist['created_at'],
	            "updated_at": gist['updated_at'],
	            "comments": gist['comments'],
	            "comments_url": gist['comments_url'],
	        }
	        cursor.execute(query, params)
    if commit:
        db.commit()
    
