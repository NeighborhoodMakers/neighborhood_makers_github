require 'birdbrain'
require_relative 'xylophone'

song = []
song.concat([ 0,0,4,4,5,5,4,Xylophone::REST ])
song.concat([ 3,3,2,2,1,1,0,Xylophone::REST ])
song.concat([ 4,4,3,3,2,2,1,Xylophone::REST ])
song.concat([ 4,4,3,3,2,2,1,Xylophone::REST ])
song.concat([ 0,0,4,4,5,5,4,Xylophone::REST ])
song.concat([ 3,3,2,2,1,1,0 ])

xylophone = Xylophone.new

xylophone.play_song(song)

xylophone.stop_song
