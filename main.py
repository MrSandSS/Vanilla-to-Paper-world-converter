import os
import tqdm
import shutil


def main():
    print('Hello!\n')

    print('Please make sure that you put your world in the Vanilla_world folder')
    print('and the "converted" folder is empty.\n')

    print('Type anything to continue')

    input()
    convert()


def convert():
    print('The converting process has started.')
    
    exceptions = ['DIM1', 'DIM-1']
    directory = [file for file in tqdm.tqdm(os.listdir('Vanilla_world'))]

    # создание папок миров (обычный, незер и энд соответственно)
    # os.mkdir('converted//world')
    # os.mkdir('converted//world_nether')
    # os.mkdir('converted//world_the_end')

    # overworld = [file for file in tqdm.tqdm(directory) if file not in exceptions]
    # the_nether = ['DIM-1']
    # the_end = ['DIM1']

    print('Converting overworld')
    tqdm.tqdm(shutil.copytree('Vanilla_World', 'converted//world', ignore=shutil.ignore_patterns('DIM1', 'DIM-1')))

    print('Converting nether')
    tqdm.tqdm(shutil.copytree('Vanilla_World//DIM-1', 'converted//world_nether//DIM-1'))

    print('Converting the end')
    tqdm.tqdm(shutil.copytree('Vanilla_World//DIM1', 'converted//world_the_end//DIM1'))


if __name__ == '__main__':
    main()
