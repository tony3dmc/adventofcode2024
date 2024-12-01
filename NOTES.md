# Commands that I need to remember

## How I configured my shell

```bash
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
. ~/.bashrc
```

## Creating the environment

```bash
pyenv install 3.12
pyenv virtualenv 3.12 adventofcode2024
```

## Activate the python environment

```bash
pyenv activate adventofcode2024
```

## Save dependencies after doing pip installs

```bash
pip freeze > requirements.txt
```
