from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import search as sr
import downloader as dl

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-q', '--query', help='Query to search for', default = None, type = str)
parser.add_argument('-l', '--list', help='Directory with list on txt file with songs to query for', default = None, type = str)
parser.add_argument('-L', '--limit', help='Limit of results', default = 10, type = int)
args = parser.parse_args()

def main():
    if not args.query and not args.list:
        print('Por favor, informe o nome da música ou o caminho do arquivo txt com as músicas!')
        return
    if args.query:
        print(f'Pesquisando por {args.query}')
        results, type = sr.search(args.query, args.limit)
        formatted_results = sr.format_results(results, type)
        if type:
            print(f'{formatted_results}')
            index = int(input('Digite o número da música:\n> ')) - 1
            download = dl.download_video(results[index]['id'], results[index]['title'])
            if download:
                print('Download concluído!')
        else:
            print(f'{formatted_results}')
            index = int(input('Digite o número da playlist:\n> ')) - 1
            download = dl.download_playlist(results[index]['id'], results[index]['title'])
            if download:
                print('Download concluído!')
    if args.list:
        with open(args.list, 'r') as file:
            for line in file:
                print(f'Pesquisando por {line}')
                results, type = sr.search(line, args.limit)
                formatted_results = sr.format_results(results, type)
                if type:
                    print(f'{formatted_results}')
                    index = int(input('Digite o número da música:\n> ')) - 1
                    download = dl.download_video(results[index]['id'], results[index]['title'])
                    if download:
                        print('Download concluído!')
                else:
                    print(f'{formatted_results}')
                    index = int(input('Digite o número da playlist:\n> ')) - 1
                    download = dl.download_playlist(results[index]['id'], results[index]['title'])
                    if download:
                        print('Download concluído!')
                print('-' * 50)

if __name__ == '__main__':
    main()