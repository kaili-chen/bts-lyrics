# Legend for lyrics.csv

* id (int) : numerical id to identify track
* album_title (string) : title of the album
* eng_album_title (string) : title of album without non-english characters
* album_seq (int) : sequence of track in album
* album_rd (string) : date that album was released in isoformat(YYYY-MM-DD)
* track_title (string) : title of the track
* kor_track_title (string) : title of the track with korean characters
* eng_track_title (string) : title of the track with only english characters
* lyrics (string) : english translated lyrics of the track (from genius)
* hidden_track (boolean) : indicates whether the track is a hidden track
* remix (boolean) : indicates whether the track is a remix
* featured (string) : indicates who is featured in the track
    * if None/NIL: "NA" reflected
* performed_by (string) : indicates who performed the track
    * multiple individuals seperated with ";" (e.g. "RM;SUGA;J-HOPE" would mean that the track is performed by RM, SUGA and J-HOPE)
    * featured artists will not be reflected in this column
* repackaged (boolean) : indicates if the track was already released in an earlier album
* language (string) : language of track
    * KOR: Korean
    * ENG: English
