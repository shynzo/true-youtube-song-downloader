import youtubesearchpython as ysp

def search(query: str, limit: int | None = 10) -> list:
    '''Search for video or playlist on YouTube.
    
    Args:
        query (str): Search query.
        limit (int, optional): Number of results to return. Defaults to 10.
    
    Returns:
        list: List of results formatted with only useful info.
        bool: type of result (video or playlist): Video = True, Playlist = False
    
    Example:
        >>> search('hello world', 5)
        >>> [
                {
                    'titulo': 'Hello World', 
                    'id': '123,
                    'time': '1:23',
                    'publishedTime': '5 years ago',
                    'views': '389M views'
                }
            ], True
    '''
    
    if 'playlist' in query:
        search = ysp.PlaylistsSearch(query, limit).result()
        results_parser: dict = search['result']
        results_formatted: list = []
        for item in results_parser:
            results_formatted.append({
                'title': item['title'],
                'id': item['id'],
                'videoCount': item['videoCount'],
            })
        return results_formatted, False
    search = ysp.VideosSearch(query, limit=limit).result()
    results_parser: dict = search["result"]
    results_formatted: list = []
    for item in results_parser:
        results_formatted.append({
            'title': item['title'],
            'id': item['id'],
            'time': item['duration'],
            'publishedTime': item['publishedTime'],
            'views': item['viewCount']['short']
        })
    return results_formatted, True

def format_results(results: list, type: bool) -> str:
    '''Format results to be sent to the user.
    
    Args:
        results (list): List of results.
        type (bool): Type of result (video or playlist): Video = True, Playlist = False
    
    Returns:
        str: Formatted results.
    
    Example:
        >>> format_results([
                {
                    'title': 'Hello World', 
                    'id': '123,
                    'time': '1:23',
                    'publishedTime': '5 years ago',
                    'views': '389M views'
                }
            ], True)
        >>> '1. Hello World (1:23) - 389M views - 5 years ago'
    '''
    
    if type:
        formatted_results: str = ''
        for i, result in enumerate(results):
            formatted_results += f'{i + 1}. {result["title"]} ({result["time"]}) | {result["views"]} | {result["publishedTime"]}\n'
        return formatted_results
    else:
        formatted_results: str = ''
        for i, result in enumerate(results):
            formatted_results += f'{i + 1}. {result["title"]} ({result["videoCount"]} videos)\n'
        return formatted_results