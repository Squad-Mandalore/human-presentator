# human presentor

## General

The project uses [uv](https://github.com/astral-sh/uv) as package manager.
And [ruff](https://github.com/astral-sh/ruff) as linter / formatter.

## Description

### Voice recognition

Done by [Zonos](https://github.com/Zyphra/Zonos)

### Face animation

Done by [Memo](https://github.com/memoavatar/memo)

### Validation of mp4

Done by [ChatGPT](https://chatgpt.com)

Testing done by SquadMandalore ChatGPT-API key

Optionally available for normal users too with own ChatGPT-API key

### optional features

- UI

- speech recording and automatic making of an mp3

- facecam support

- windows (not planned)

## Process

Zonos and Memo are APIs while the human-presentor is the client which combines both libraries.
General idea is that the client splits the work into slides so that both libraries can work simultaneously.

## Risks

GPU cannot handle both applications at the same time.
Docker Container need the nvidia container toolkit.
Fast API is not good with file sending.
