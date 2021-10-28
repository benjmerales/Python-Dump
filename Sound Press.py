import winsound as W
import keyboard

alist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
	if keyboard.is_pressed('a'):
		W.PlaySound(None, W.SND_PURGE)