#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Feb 22 11:36:53 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
#Child Id und Altersgruppe kann zur Vorbereitung hier eingegeben werden
childID = "test"
#ganze Zahl eingeben, Auswahl: 2, 3 oder 4
childAge = 4


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy import monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

#Zusätzlich zu den default imports
import datetime
import pandas as pd
import csv
import glob
import wave



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Pylex_neu'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
language_list = os.listdir("sound_files")
exclude = ["arabic", "._.DS_Store",".DS_Store"] #exclude certain languages from being used (if for example not all sound files are present)
language_list = [x for x in language_list if x not in exclude]
language_list = sorted(language_list) #sort list alphabetically
language_list = sorted(language_list, key=lambda x: x not in ['american_english', 'french', 'spanish', 'italian'])
 

# check if childID is a string
if not isinstance(childID, str):
    # if not, convert it to a string
    childID = str(childID)

# check if childAge is a string
if not isinstance(childAge, str):
    # if not, convert it to a string
    childAge = str(childAge)
    
ageList = ["2","3","4"] # check if input Age is in List of possible ages
if not childAge in ageList: # check if the input childAge is in the ageList
    while 1: # start an infinite loop
        dlg = gui.Dlg(title = "Age Error") # create a dialog box with the title "Age Error"
        dlg.addText("Child Age is not as it should be,  please choose one of the following age ranges") # add text to the dialog box
        dlg.addField('Age Group:', choices=["2","3","4"]) # add a dropdown menu to the dialog box where the user can choose an age group
        age_error = dlg.show() # show the dialog box and store the user's selection in the variable age_error
        if dlg.OK == False: # if the user clicked the cancel button, quit the experiment
            core.quit()  
        elif dlg.OK: # if the user clicked the OK button, break out of the loop
            break
    childAge = age_error[0] # update the childAge variable to the user's selection


    


# GUI to enter subject information and change experiment options
while 1:
    dlg = gui.Dlg(title=expName)
    dlg.addText("Subject Info")
    dlg.addField('Subject ID:', initial = childID) # adds a field for the subject ID with a default value of childID
    dlg.addField('Age Group:', choices=["2","3","4"], initial = childAge) # adds a dropdown field for age group with default value of childAge
    dlg.addField('Language:', choices=language_list, initial = "swiss_german") # adds a dropdown field for language with default value of "swiss_german"
    dlg.addField('Reference Language?', initial = True) # adds a checkbox field for choosing reference language with default value of True
    dlg.addField('Screen flipped?', initial = True) # adds a checkbox field for choosing screen orientation with default value of False
    dlg.addField('Touchscreen', initial = True) # adds a checkbox field for choosing input device with default value of False
    subject_details = dlg.show() # displays the dialog and stores the input values in subject_details
    if dlg.OK == False:
        core.quit()  # exits the program if user pressed cancel
    elif dlg.OK:
        break # breaks out of the loop if user pressed OK to confirm the input

age = subject_details[1] # retrieves the age group value from the subject_details list
age = subject_details[1]

if int(age) < 3:
    max_time = 12 # if subject is below 3 years, give 12 seconds to respond
else:
    max_time = 7 # otherwise give 7 seconds to respond

if subject_details[3]: # checks if the user chose to test in the reference language
    type = 'std' # sets the type variable to 'std' if it's the reference language
else:
    type = 'other' # sets the type variable to 'other' if it's not the reference language

if subject_details[4]: # checks if the user chose to flip the screen orientation
    viewOri = 90 # sets the view orientation to 90 degrees if the screen is flipped
    points_pos = (0,-30) # sets the position of the points stimulus accordingly
    text_pos = (0,100) # sets the position of the text stimulus accordingly
else:
    viewOri = 0 # sets the view orientation to 0 degrees if the screen is not flipped
    points_pos = (0,30) # sets the position of the points stimulus accordingly
    text_pos = (0,-100) # sets the position of the text stimulus accordingly

delay = 0.5 #don't play trial sound imediataley, delay start of sound for x seconds

now = datetime.datetime.now()

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
log_filename = os.path.join("log_files","".join([subject_details[0],'_',subject_details[2],'.csv']))
filename = os.path.join("trial_lists","".join(["age",age,"_",type,".xlsx"])) # select corresponding trial list
trial_list = pd.read_excel(filename,header=None) # read trial list

# Create file headers and add time stamp
curr_part_file = open(os.path.join('log_files',"".join([subject_details[0],'_',subject_details[2],'.csv'])),'wt') # open experiment file
write_to_file = csv.writer(curr_part_file, delimiter='\t', quoting=csv.QUOTE_NONE)
write_to_file.writerow([now.strftime("%Y-%m-%d %H:%M")])#adds time and to top of file
write_to_file.writerow(['subject_id','language','randomization','time','name_sound','ans_correct', 'ans_wrong', 'missed','clicked item', 'correct item']) # write header to file
#same steps for second file quick and dirty
file_quickAndDirty = open(os.path.join('log_files',"".join([subject_details[0],'_', "quickAndDirty", "_",subject_details[2],'.csv'])),'wt') #open second file
write_to_quickAndDirty = csv.writer(file_quickAndDirty, delimiter='\t', quoting=csv.QUOTE_NONE)
write_to_quickAndDirty.writerow([now.strftime("%Y-%m-%d %H:%M")])#adds time and to top of file
curr_part_file.flush()
file_quickAndDirty.flush()




# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/salomewenk/Library/CloudStorage/OneDrive-UniversitätZürichUZH/Universität/23 FS/Praktikum/my_version_billex/my_version.py',
    savePickle=False, saveWideText=False,
    dataFileName=log_filename)

logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation



# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate() # get the actual frame rate of the monitor
if expInfo['frameRate'] != None: # if the frame rate can be measured
    frameDur = 1.0 / round(expInfo['frameRate']) # calculate the duration of each frame
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess (assuming a frame rate of 60 frames per second)

# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy') # set up the iohub keyboard and specify to use psychopy key mapping

ioSession = '1' # initialize the session number to '1'
if 'session' in expInfo: # if the 'session' key is in the experiment information
    ioSession = str(expInfo['session']) # set the session number to the value associated with the 'session' key

ioServer = io.launchHubServer(window=win, **ioConfig) # launch the iohub server with the window and input device configurations
eyetracker = None # set the eyetracker to None (not using it in this experiment)

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "white" ---
# Create an image stimulus named "White", with the given properties:
White = visual.ImageStim(
    win=win, # draw on the window 'win'
    name='White', # stimulus name
    image='pictures/white.jpg', # image file to display
    mask=None, # no image mask
    anchor='center', # set the anchor point to the center of the image
    ori=0.0, # set the orientation of the image to 0 degrees
    pos=(0, 0), # set the position of the image to (0, 0) which is the center of the screen
    size=(1.333, 1), # set the size of the image to be 1.333 times wider than it is tall
    color=[1.333,1], # multiply the RGB color of the image by [1.333, 1, 1], which effectively makes the image brighter
    colorSpace='rgb', # use the RGB color space
    opacity=None, # do not set the opacity of the image
    flipHoriz=False, # do not flip the image horizontally
    flipVert=False, # do not flip the image vertically
    texRes=128.0, # set the texture resolution of the image to 128
    interpolate=True, # use linear texture interpolation
    depth=0.0) # set the depth of the image to 0

# Create a keyboard component named 'key_resp_2'
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "familiarization" ---
#sound and image files are not selected here but rather during the trial to update them during the experiment, is a reliect of psychopy builder
sound_1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0) # set the volume of sound_1 to full volume (1.0)
sound_2 = sound.Sound('B', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0) # set the volume of sound_2 to full volume (1.0)
key_resp = keyboard.Keyboard() # Create a keyboard object to capture participant's key presses
image_familiarization = visual.ImageStim(
    win=win,
    name='image_familiarization', 
    image='pictures/hund.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3333,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Create a list of familiarization items, which are used to select the corresponding image and sound files
familiarization_items = ["hund", "apfel"]




# --- Initialize components for Routine "trial" ---
totalTime = 0
top_left = visual.Rect(
    win=win, name='top_left',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(-0.444, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0, 0.0, 0.0],
    opacity=None, depth=0.0, interpolate=True)#depth defines if image is in front or in the back (order of images/shapes)
top_middle = visual.Rect(
    win=win, name='top_middle',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0, 1.0, 0.0],
    opacity=None, depth=-1.0, interpolate=True)
top_right = visual.Rect(
    win=win, name='top_right',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(0.444, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0, 0.0, 1.0],
    opacity=None, depth=-2.0, interpolate=True)
bottom_left = visual.Rect(
    win=win, name='bottom_left',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(-0.444, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0, 1.0, 0.0],
    opacity=None, depth=-3.0, interpolate=True)
bottom_middle = visual.Rect(
    win=win, name='bottom_middle',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(0, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.5, 0.0, 0.5],
    opacity=None, depth=-4.0, interpolate=True)
bottom_right = visual.Rect(
    win=win, name='bottom_right',
    width=(0.444, 0.5)[0], height=(0.333, 0.5)[1],
    ori=0.0, pos=(0.444, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0, 0.5, 0.0],
    opacity=None, depth=-5.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.33333,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
trial_sound = sound.Sound('A', secs=max_time, stereo=True, hamming=True,
    name='trial_sound')
trial_sound.setVolume(1.0)
trial_mouse = event.Mouse(win=win) #original
x, y = [None, None]
trial_mouse.mouseClock = core.Clock()


#Flip the window if selected for trial
trialComponents = [top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right, image, trial_sound, trial_mouse]
familiarizationComponents = []
if subject_details[4]:
    for thisComponent in trialComponents:
        thisComponent.flipVert = True
        thisComponent.flipHoriz = True
    trialAreas = [top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right]
    for thisArea in trialAreas:
        thisArea.pos = thisArea.pos * -1
    image_familiarization.flipVert = True
    image_familiarization.flipHoriz = True




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "white" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
whiteComponents = [White, key_resp_2]
for thisComponent in whiteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "white" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *White* updates
    if White.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White.frameNStart = frameN  # exact frame index
        White.tStart = t  # local t and not account for scr refresh
        White.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'White.started')
        White.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in whiteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "white" ---
for thisComponent in whiteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "white" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


#select correct trial_file to read from (decides wich image/sound to play)
if subject_details[3]:
    trial_file = "trial_lists/age" + age + "_std.xlsx"   
else:
    trial_file = "trial_lists/age" + age + "_other.xlsx"   

# set up handler to look after randomisation of conditions etc
familiarization_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='familiarization_loop')
familiarization_nr = 0 #to start at 0
thisExp.addLoop(familiarization_loop)  # add the loop to the experiment
thisFamiliarization_loop = familiarization_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFamiliarization_loop.rgb)
if thisFamiliarization_loop != None:
    for paramName in thisFamiliarization_loop:
        exec('{} = thisFamiliarization_loop[paramName]'.format(paramName))

for thisFamiliarization_loop in familiarization_loop:
    currentLoop = familiarization_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFamiliarization_loop.rgb)
    if thisFamiliarization_loop != None:
        for paramName in thisFamiliarization_loop:
            exec('{} = thisFamiliarization_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "familiarization" ---
    continueRoutine = True
    routineForceEnded = False
    
    #update image
    if subject_details[3]:
        image_familiarizationFile = os.path.join("pictures","".join([familiarization_items[familiarization_nr],'.jpg']))
    else:
        image_familiarizationFile = os.path.join("pictures","".join(["ot_", familiarization_items[familiarization_nr],'.jpg']))
    #update sound
    soundFile_1 = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_',familiarization_items[familiarization_nr],'.wav'])))[0]
    soundFile_2 = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_w_i_',familiarization_items[familiarization_nr],'.wav'])))[0]

    #Calculate duration of sound 1
    with wave.open(soundFile_1, 'r') as wav_file:
        # Get the number of frames
        num_frames = wav_file.getnframes()    
        # Get the frame rate (sample rate)
        frame_rate = wav_file.getframerate()
        # Calculate the duration in seconds
        duration = num_frames / float(frame_rate)

    # update component parameters for each repeat
    image_familiarization.setImage(image_familiarizationFile)
    sound_1.setSound(soundFile_1, secs=duration, hamming=True)
    sound_1.setVolume(1.0, log=False)
    sound_2.setSound(soundFile_2, hamming=True)
    sound_2.setVolume(1.0, log=False)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    familiarizationComponents = [sound_1, sound_2, key_resp, image_familiarization]
    for thisComponent in familiarizationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "familiarization" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                sound_1.stop()
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= duration-frameTolerance: #sound 2 starts after sound 1 is finished
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2.started', tThisFlipGlobal)
            sound_2.play(when=win)  # sync with win flip
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['right','space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_familiarization* updates
        if image_familiarization.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_familiarization.frameNStart = frameN  # exact frame index
            image_familiarization.tStart = t  # local t and not account for scr refresh
            image_familiarization.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_familiarization, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_familiarization.started')
            image_familiarization.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            
        if defaultKeyboard.getKeys(keyList=["left"]): #restart the trial with left arrow key
            routineForceEnded = True
                # --- Ending Routine "familiarization" ---
            for thisComponent in familiarizationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            sound_1.stop()  # ensure sound has stopped at end of routine
            sound_2.stop()  # ensure sound has stopped at end of routine
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            thisExp.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                thisExp.addData('key_resp.rt', key_resp.rt)
            routineTimer.reset()
                
            # --- Prepare to restart Routine "familiarization" ---
            continueRoutine = True
            routineForceEnded = False
            
            #update image
            if subject_details[3]:
                image_familiarizationFile = os.path.join("pictures","".join([familiarization_items[familiarization_nr],'.jpg']))
            else:
                image_familiarizationFile = os.path.join("pictures","".join(["ot_", familiarization_items[familiarization_nr],'.jpg']))
            #update sound
            soundFile_1 = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_',familiarization_items[familiarization_nr],'.wav'])))[0]
            soundFile_2 = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_w_i_',familiarization_items[familiarization_nr],'.wav'])))[0]

            #Calculate duration of sound 1
            with wave.open(soundFile_1, 'r') as wav_file:
                # Get the number of frames
                num_frames = wav_file.getnframes()    
                # Get the frame rate (sample rate)
                frame_rate = wav_file.getframerate()
                # Calculate the duration in seconds
                duration = num_frames / float(frame_rate)

            # update component parameters for each repeat
            image_familiarization.setImage(image_familiarizationFile)
            sound_1.setSound(soundFile_1, secs=duration, hamming=True)
            sound_1.setVolume(1.0, log=False)
            sound_2.setSound(soundFile_2, hamming=True)
            sound_2.setVolume(1.0, log=False)
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            familiarizationComponents = [sound_1, sound_2, key_resp, image_familiarization]
            for thisComponent in familiarizationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familiarizationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "familiarization" ---
    for thisComponent in familiarizationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    sound_2.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.nextEntry()
    # the Routine "familiarization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    familiarization_nr = familiarization_nr+1
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'familiarization_loop'




# set up handler to look after randomisation of conditions etc for trial
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(trial_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

#set all variables to 0
trial_nr = 0
korrekt = 0
incorrect = 0.0
missed = 0.0
for thisTrial in trials:
    trial_nr = trial_nr + 1 #count trial numbers for image and sound
    currentLoop = trials

    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    win.flip()
    core.wait(1.5)
    continueRoutine = True
    routineForceEnded = False
    #update image
    image_file = os.path.join("pictures","".join([trial_list.iloc[trial_nr,1],'.jpg']))
    #update sound
    sound_file = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_',trial_list.iloc[trial_nr,0],'.wav'])))[0]
    # update component parameters for each repeat
    image.setImage(image_file)
    trial_sound.setSound(sound_file, secs=max_time, hamming=True)
    trial_sound.setVolume(1.0, log=False)
    # setup some python lists for storing info about the trial_mouse
    trial_mouse.x = []
    trial_mouse.y = []
    trial_mouse.leftButton = []
    trial_mouse.midButton = []
    trial_mouse.rightButton = []
    trial_mouse.time = []
    trial_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < max_time:
        #output to file is allways 0 or 1 (if answered correct / incorrect etc.) reset of variables to 0 is needed after each repeat
        thisRoundincorrect = 0
        thisRoundkorrekt = 0
        thisRoundmissed = 0
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *top_left* updates
        if top_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_left.frameNStart = frameN  # exact frame index
            top_left.tStart = t  # local t and not account for scr refresh
            top_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_left, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'top_left.started')
            top_left.setAutoDraw(True)
        if top_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > top_left.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                top_left.tStop = t  # not accounting for scr refresh
                top_left.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'top_left.stopped')
                top_left.setAutoDraw(False)
        
        # *top_middle* updates
        if top_middle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_middle.frameNStart = frameN  # exact frame index
            top_middle.tStart = t  # local t and not account for scr refresh
            top_middle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_middle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'top_middle.started')
            top_middle.setAutoDraw(True)
        if top_middle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > top_middle.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                top_middle.tStop = t  # not accounting for scr refresh
                top_middle.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'top_middle.stopped')
                top_middle.setAutoDraw(False)
        
        # *top_right* updates
        if top_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_right.frameNStart = frameN  # exact frame index
            top_right.tStart = t  # local t and not account for scr refresh
            top_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_right, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'top_right.started')
            top_right.setAutoDraw(True)
        if top_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > top_right.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                top_right.tStop = t  # not accounting for scr refresh
                top_right.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'top_right.stopped')
                top_right.setAutoDraw(False)
        
        # *bottom_left* updates
        if bottom_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_left.frameNStart = frameN  # exact frame index
            bottom_left.tStart = t  # local t and not account for scr refresh
            bottom_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_left, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bottom_left.started')
            bottom_left.setAutoDraw(True)
        if bottom_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottom_left.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                bottom_left.tStop = t  # not accounting for scr refresh
                bottom_left.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bottom_left.stopped')
                bottom_left.setAutoDraw(False)
        
        # *bottom_middle* updates
        if bottom_middle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_middle.frameNStart = frameN  # exact frame index
            bottom_middle.tStart = t  # local t and not account for scr refresh
            bottom_middle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_middle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bottom_middle.started')
            bottom_middle.setAutoDraw(True)
        if bottom_middle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottom_middle.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                bottom_middle.tStop = t  # not accounting for scr refresh
                bottom_middle.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bottom_middle.stopped')
                bottom_middle.setAutoDraw(False)
        
        # *bottom_right* updates
        if bottom_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_right.frameNStart = frameN  # exact frame index
            bottom_right.tStart = t  # local t and not account for scr refresh
            bottom_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_right, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bottom_right.started')
            bottom_right.setAutoDraw(True)
        if bottom_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottom_right.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                bottom_right.tStop = t  # not accounting for scr refresh
                bottom_right.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bottom_right.stopped')
                bottom_right.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        # start/stop trial_sound
        if trial_sound.status == NOT_STARTED and tThisFlip >= delay-frameTolerance:
            # keep track of start time/frame for later
            trial_sound.frameNStart = frameN  # exact frame index
            trial_sound.tStart = t  # local t and not account for scr refresh
            trial_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('trial_sound.started', tThisFlipGlobal)
            trial_sound.play(when=win)  # sync with win flip
        if trial_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_sound.tStartRefresh + max_time-frameTolerance: #change here
                # keep track of stop time/frame for later
                trial_sound.tStop = t  # not accounting for scr refresh
                trial_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_sound.stopped')
                trial_sound.stop()
        # *trial_mouse* updates
        if trial_mouse.status == NOT_STARTED and t >= delay-frameTolerance:
            # keep track of start time/frame for later
            trial_mouse.frameNStart = frameN  # exact frame index
            trial_mouse.tStart = t  # local t and not account for scr refresh
            trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('trial_mouse.started', t)
            trial_mouse.status = STARTED
            trial_mouse.mouseClock.reset()
            prevButtonState = trial_mouse.getPressed()  # if button is down already this ISN'T a new click
            prevPositionState = trial_mouse.getPos()
        if trial_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_mouse.tStartRefresh + max_time-frameTolerance:
                # keep track of stop time/frame for later
                trial_mouse.tStop = t  # not accounting for scr refresh
                trial_mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('trial_mouse.stopped', t)
                trial_mouse.status = FINISHED
        if not subject_details[5]: #in this case working with mouse, looking out for button presses
            if trial_mouse.status == STARTED:  # only update if started and not finished!
                buttons = trial_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right])
                            clickableList = [top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right]
                        except:
                            clickableList = [[top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right]]
                        for obj in clickableList:
                            if obj.contains(trial_mouse):
                                gotValidClick = True
                                trial_mouse.clicked_name.append(obj.name)
                        x, y = trial_mouse.getPos()
                        trial_mouse.x.append(x)
                        trial_mouse.y.append(y)
                        buttons = trial_mouse.getPressed()
                        trial_mouse.leftButton.append(buttons[0])
                        trial_mouse.midButton.append(buttons[1])
                        trial_mouse.rightButton.append(buttons[2])
                        trial_mouse.time.append(trial_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
        else: #working with a Touchscreen
            if trial_mouse.status == STARTED:  # only update if started and not finished!
                position = trial_mouse.getPos()
                if position[0] != prevPositionState[0] or position[1] != prevPositionState[1]:  # button state changed?
                    gotValidClick = False
                    try:
                        iter([top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right])
                        clickableList = [top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right]
                    except:
                        clickableList = [[top_left, top_middle, top_right, bottom_left, bottom_middle, bottom_right]]
                    for obj in clickableList:
                        if obj.contains(trial_mouse):
                            gotValidClick = True
                            trial_mouse.clicked_name.append(obj.name)
                    x, y = trial_mouse.getPos()
                    trial_mouse.x.append(x)
                    trial_mouse.y.append(y)
                    buttons = trial_mouse.getPressed()
                    trial_mouse.leftButton.append(buttons[0])
                    trial_mouse.midButton.append(buttons[1])
                    trial_mouse.rightButton.append(buttons[2])
                    trial_mouse.time.append(trial_mouse.mouseClock.getTime())
                    if gotValidClick:
                        prevPositionState = position
                        continueRoutine = False  # abort routine on response
                        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if defaultKeyboard.getKeys(keyList=["space"]): 
            continueRoutine = False
            trials.finished = True
            missed = missed -1
        if defaultKeyboard.getKeys(keyList=["p"]): #pause trial with p and restart it once p is pressed again
            isitpaused = True
            routineForceEnded = True
            continueRoutine = False
            # ending Routine
            # --- Ending Routine "trial" ---
            #for thisComponent in trialComponents:
            #    if hasattr(thisComponent, "setAutoDraw"):
            #        thisComponent.setAutoDraw(False)
            #trial_sound.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            #if routineForceEnded:
            #    routineTimer.reset()
            #else:
            #    routineTimer.addTime(-max_time)
            while isitpaused == True: 
                event.waitKeys()
                routineTimer.reset()
                #starting Routine
                continueRoutine = True
                routineForceEnded = False
                #update image
                image_file = os.path.join("pictures","".join([trial_list.iloc[trial_nr,1],'.jpg']))
                #update sound
                sound_file = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_',trial_list.iloc[trial_nr,0],'.wav'])))[0]
                # update component parameters for each repeat
                image.setImage(image_file)
                trial_sound.setSound(sound_file, secs=max_time, hamming=True)
                trial_sound.setVolume(1.0, log=False)
                # setup some python lists for storing info about the trial_mouse
                trial_mouse.x = []
                trial_mouse.y = []
                trial_mouse.leftButton = []
                trial_mouse.midButton = []
                trial_mouse.rightButton = []
                trial_mouse.time = []
                trial_mouse.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                for thisComponent in trialComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                isitpaused = False
                break
                    
        if defaultKeyboard.getKeys(keyList=["left"]): #restart the trial with left arrow key
            routineForceEnded = True
            # ending Routine
            # --- Ending Routine "trial" ---
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_sound.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-max_time)
            #starting Routine
            continueRoutine = True
            routineForceEnded = False
            #update image
            image_file = os.path.join("pictures","".join([trial_list.iloc[trial_nr,1],'.jpg']))
            #update sound
            sound_file = glob.glob(os.path.join("sound_files",subject_details[2],"".join(['??_',trial_list.iloc[trial_nr,0],'.wav'])))[0]
            # update component parameters for each repeat
            image.setImage(image_file)
            trial_sound.setSound(sound_file, secs=max_time, hamming=True)
            trial_sound.setVolume(1.0, log=False)
            # setup some python lists for storing info about the trial_mouse
            trial_mouse.x = []
            trial_mouse.y = []
            trial_mouse.leftButton = []
            trial_mouse.midButton = []
            trial_mouse.rightButton = []
            trial_mouse.time = []
            trial_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
                    
                    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
            
    #count correct answers
    korrekte_antwort = "['" + trial_list.iloc[trial_nr,2] + "']"
    if str(korrekte_antwort) == str(trial_mouse.clicked_name):
        korrekt = korrekt + 1
        thisRoundkorrekt = 1
    elif str(trial_mouse.clicked_name) == "[]":
        missed = missed + 1
        thisRoundmissed = 1
    else:
        incorrect = incorrect + 1
        thisRoundincorrect = 1
        
        
    time = routineTimer.getTime()
    totalTime = totalTime + time
    #write the results to log file original commented out
    #write_to_file.writerow([subject_details[0],subject_details[2],type,trial_time.getTime(),trial_list.iloc[trial_nr,1],x,y,trial_time.getTime()-word_onset,1])
    write_to_file.writerow([subject_details[0],subject_details[2],type,time, trial_list.iloc[trial_nr,0],thisRoundkorrekt, thisRoundincorrect, thisRoundmissed, trial_mouse.clicked_name, trial_list.iloc[trial_nr, 2]])
    curr_part_file.flush()

    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_sound.stop()  # ensure sound has stopped at end of routine
    # store data for trials (TrialHandler)
    trials.addData('trial_mouse.x', trial_mouse.x)
    trials.addData('trial_mouse.y', trial_mouse.y)
    trials.addData('trial_mouse.leftButton', trial_mouse.leftButton)
    trials.addData('trial_mouse.midButton', trial_mouse.midButton)
    trials.addData('trial_mouse.rightButton', trial_mouse.rightButton)
    trials.addData('trial_mouse.time', trial_mouse.time)
    trials.addData('trial_mouse.clicked_name', trial_mouse.clicked_name)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-max_time)
    thisExp.nextEntry()
        
    
# completed 1.0 repeats of 'trials'

#Prozent korrekt berechnen
perc_correct = (korrekt/(korrekt+incorrect+missed))*100
# write results in last line
write_to_quickAndDirty.writerow(['Child ID: ', subject_details[0]])
write_to_quickAndDirty.writerow(['Language: ',subject_details[2]])
write_to_quickAndDirty.writerow(['Randomization: ', type])
write_to_quickAndDirty.writerow(['Age: ', age])
write_to_quickAndDirty.writerow(['Correct Items: ',int(korrekt)])
write_to_quickAndDirty.writerow(['Incorrect Items: ',int(incorrect)])
write_to_quickAndDirty.writerow(['Missed Items: ',int(missed)])
write_to_quickAndDirty.writerow(['Percentage Correct: ',perc_correct, '%'])
write_to_quickAndDirty.writerow(['Total Time: ', totalTime])
file_quickAndDirty.flush()

# --- Initialize components for Routine "confetti" ---
confetti_image = visual.ImageStim(
    win=win,
    name='confetti_image', 
    image='pictures/confetti.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3333, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Punkte:\n\n '+ str(korrekt) , #Text auf letzter Seite, für neue Zeile: \n
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
    
#Flip the window if selected for confetti
confettiComponents = [confetti_image, text]
if subject_details[4]:
    for thisComponent in confettiComponents:
        thisComponent.flipVert = True
        thisComponent.flipHoriz = True



# --- Prepare to start Routine "confetti" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
for thisComponent in confettiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# close the csv files (makes it flush one last time)
curr_part_file.close()
file_quickAndDirty.close()


# --- Run Routine "confetti" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *confetti_image* updates
    if confetti_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        confetti_image.frameNStart = frameN  # exact frame index
        confetti_image.tStart = t  # local t and not account for scr refresh
        confetti_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confetti_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'confetti_image.started')
        confetti_image.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
        
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in confettiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "confetti" ---
for thisComponent in confettiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "confetti" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(log_filename+'.csv', delim='auto')
thisExp.saveAsPickle(log_filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
