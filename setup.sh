git clone https://github.com/tho2011/wordle_player.git

conda create -n wordle python=3.8 numpy pandas scipy tqdm
source activate wordle || conda activate wordle

cd wordle
echo "Setup completed!"
