require 'birdbrain'
require_relative 'xylophone'

song = [ 0,0,4,4,5,5,4,Xylophone::REST,3,3,2,2,1,1,0,Xylophone::REST,4,4,3,3,2,2,1,Xylophone::REST,4,4,3,3,2,2,1,Xylophone::REST,0,0,4,4,5,5,4,Xylophone::REST,3,3,2,2,1,1,0 ]

xylophone = Xylophone.new

xylophone.play_song(song)

xylophone.stop_song

=begin
from xylophone import Xylophone

song = [ 0,0,4,4,5,5,4,Xylophone.REST,3,3,2,2,1,1,0,Xylophone.REST,4,4,3,3,2,2,1,Xylophone.REST,4,4,3,3,2,2,1,Xylophone.REST,0,0,4,4,5,5,4,Xylophone.REST,3,3,2,2,1,1,0 ]

xylophone = Xylophone()

xylophone.play_song(song)

xylophone.stop_song()
=end
