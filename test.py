import sqlite3

# Connect to your database
conn = sqlite3.connect('spotify.db')  # replace with your database file
cursor = conn.cursor()

# Execute the query
query = '''
SELECT name, COUNT(*) AS song_count 
FROM song_artists sa 
JOIN artists a ON sa.artist_id = a.artist_id 
GROUP BY name 
ORDER BY song_count DESC;
'''
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Write results to a text file
with open('query_results.txt', 'w') as file:
    # Write the header
    file.write('name,song_count\n')
    
    # Write the data
    for row in results:
        file.write(f'{row[0]},{row[1]}\n')

# Close the database connection
conn.close()