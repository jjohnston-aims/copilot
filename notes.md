# Workshop day 1

Uses GPT 4 model in chat. Ghost text (inline suggestions) uses 3.5 in the backend.

Editors supported (officially):

- VS Code (new features first)
- JetBrains
- Neovim
- etc

Supported editor are covered by Github's lawyers to defend copyright claims.

workflow:

Github has a proxy between it's  GPT 4 instance.

Authenticates and removes abusive language before sending to the LLM.

Intercepts the response and does some other things.

How does context work in NeoVim? If you have a file open in another buffer will
Copilot get the context? TODO: test this

You can maximise accuracy by providing more context. This is done by adding
comments, eg, an overview in comments at the top of the file.

Try providing examples of the input and output data to give a better context.

## Microsoft Copilot

We have [Microsoft Copilot](https://copilot.microsoft.com) as an alternate to ChatGPT.

## My experience

I have been using this with NeoVim and it's beed quite good when the context has been small. With larger contexts it doesn't always get the context that you want it to get.

## Lab

- [copilot-rock-paper-scissors](https://github.com/copilot-workshops/copilot-rock-paper-scissors)
- [copilot-lab-r](https://github.com/Insight-Services-APAC/copilot-lab-r)
- [copilot-lab-sql](https://github.com/Insight-Services-APAC/copilot-lab-sql)
- [copilot-lab-music-store-typescript](https://github.com/Insight-Services-APAC/copilot-lab-music-store-typescript)
- [MicrosoftCopilotHackathon](https://github.com/GitHub-Partner-Demo-Library/MicrosoftCopilotHackathon?tab=readme-ov-file#labs-instructions)
- [MicrosoftCopilotHackathon - dataengineer](https://github.com/GitHub-Partner-Demo-Library/MicrosoftCopilotHackathon/blob/main/exercisefiles/dataengineer/README.md)
- [MicrosoftCopilotHackathon - datascientist](https://github.com/GitHub-Partner-Demo-Library/MicrosoftCopilotHackathon/blob/main/exercisefiles/datascientist/README.md)
- [github-copilot-labs-list](https://github.com/Insight-Services-APAC/github-copilot-labs-list?tab=readme-ov-file)

## Other reading

[Secret Sauce 1: Prompt Engineering](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html#secret-sauce-1-prompt-engineering)

## Copilot API

[Installing github copilot in the cli](https://docs.github.com/en/copilot/github-copilot-in-the-cli/installing-github-copilot-in-the-cli)
