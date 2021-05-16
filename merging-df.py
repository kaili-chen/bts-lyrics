# grouping by total number of tracks
total = unfiltered_df.copy()[['album_title','track_title', 'id']]
total = total.groupby(by='album_title', as_index=False).agg({
    'track_title': 'count',
    'id': 'min'
    }).sort_values(by=['id'])
total = total.rename(columns={
    'track_title': 'total_tracks'
})

# grouping by unique tracks
unique = df.copy()[['album_title','track_title', 'id']]
unique = unique.groupby(by='album_title', as_index=False).agg({
    'track_title': 'count',
    'id': 'min'
    }).sort_values(by=['id'])
unique = unique.rename(columns={
    'track_title': 'unique_tracks'
})

# merging the 2 different 
combined = total.merge(unique, on='album_title')
combined = combined.drop(columns='id_y')
combined = combined.rename(columns={'id_x': 'id'})

# plot
plt.title('Number of Tracks By Album')
plt.ylabel('# tracks')
plt.xlabel('album')
plt.xticks(rotation=90)

plt.bar('album_title', 'total_tracks', data=combined, color='#8878af', label='# tracks')
plt.bar('album_title', 'unique_tracks', data=combined, color='#c76e6e', label='# unique tracks')

plt.legend(loc='upper left')

# add data labels
for x, y1, y2 in zip(combined['album_title'], combined['total_tracks'], combined['unique_tracks']):
    plt.text(x, y2+0.2, y2, ha='center', size='x-small', color='white')
    plt.text(x, y1+0.2, y1, ha='center', size='x-small', color='black')

# save plot as png
plt.savefig('img/plots/02_num_tracks_album_bar.png', bbox_inches='tight')