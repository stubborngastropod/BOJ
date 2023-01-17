{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input())\n",
    "meetings = []\n",
    "meetingnum = 1\n",
    "\n",
    "for i in range(N):\n",
    "    m = list(map(int, input().split()))\n",
    "    meetings.append(m)\n",
    "\n",
    "meetings.sort(key = lambda x: (x[1], x[0]))\n",
    "\n",
    "endtime = meetings[0][1]\n",
    "\n",
    "for i in range(1, N):\n",
    "    if meetings[i][0] >= endtime:\n",
    "        meetingnum += 1\n",
    "        endtime = meetings[i][1]\n",
    "\n",
    "print(meetingnum)"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
