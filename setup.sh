git clone https://github.com/tho2011/wordle_player.git

conda create -n wordle python=3.8 numpy pandas scipy tqdm colorama matplotlib ipykernel jupyterlab
source activate wordle || conda activate wordle

cd wordle_player
echo "Setup completed!"
