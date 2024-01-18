from optparse import OptionParser
import json
import os
from random import randint

def gen_dict():
    return {
        "Contributors": [
            "Swaroop Mishra",
            "Daniel Khashabi"
        ],
        "Source": [
            "MultiLexNorm: Multilingual Lexical Normalization"
        ],
        "URL": [
            "https://noisy-text.github.io/2021/multi-lexnorm.html"
        ],
        "Categories": [
            "Lexical Normalization"
        ],
        "Reasoning": [
            "Temporal Reasoning",
            "Commonsense Reasoning"
        ],
        "Definition": [
            "Lexical norm"
        ],
        "Input_language": [
            "Multilanguage"
        ],
        "Output_language": [
            "Multilanguage"
        ],
        "Instruction_language": [
            "Multilanguage"
        ],
        "Domains": [
            "Twitter",
            "Arto",
            "sms",
            "forum",
        ],
        "Positive Examples": [],
        "Negative Examples": [],
        "Instances": [],
        "Instance License": [
            "Unknown"
        ]
    }


def convert_to_json(file_name, input_path, output_path, json_name, task_id):
    data_dict_list = []
    idx = 0
    curSent = []
    final_data = gen_dict()
    input_file_path = os.path.join(input_path, file_name)

    with open(input_file_path) as in_file:
        for line in in_file:
            tok = line.strip().split('\t')

            if tok == [''] or tok == []:
                data_dict_list.append({
                    "id": task_id + "-" + str(idx),
                    "input": ' '.join([x[0] for x in curSent]),
                    "output": [' '.join([x[1] for x in curSent])]
                })
                curSent = []
                idx += 1

            else:
                if len(tok) > 2:
                    err('erroneous input, line:\n' + line + '\n in file ' + input_file_path + ' contains more then two elements')
                if len(tok) == 1:
                    tok.append('')
                curSent.append(tok)

        # in case file does not end with newline
        if curSent != []:
            data_dict_list.append({
                    "id": task_id + "-" + str(idx),
                    "input": ' '.join([x[0] for x in curSent]),
                    "output": [' '.join([x[1] for x in curSent])]
                })
        random_ints = [randint(0, len(data_dict_list)), randint(0, len(data_dict_list)), randint(0, len(data_dict_list))]
        positive_examples = [
            {
                'input': data_dict_list[random_ints[0]]['input'],
                'output': data_dict_list[random_ints[0]]['output'][0],
                'explanation': "The text is now lexically normalized and correct."
            },
            {
                'input': data_dict_list[random_ints[1]]['input'],
                'output': data_dict_list[random_ints[1]]['output'][0],
                'explanation': "The text is now lexically normalized and correct."
            }
        ]
        negative_examples = [
            {
                'input': data_dict_list[random_ints[2]]['input'],
                'output': data_dict_list[random_ints[2]]['output'][0],
                'explanation': "The text is not lexically normalized and it is incorrect."
            }
        ]
        final_data['Instances'] = data_dict_list
        final_data["Positive Examples"] = positive_examples
        final_data["Negative Examples"] = negative_examples
    with open(os.path.join(output_path, json_name), "w", encoding="utf-8") as out_file:
        json.dump(final_data, out_file, indent=2, ensure_ascii=False)


def process_language_tasks(data_path, output_path, language_name, lang_id):
    tasks = ['train', 'test']

    for task in tasks:
        actual_id = f'task{lang_id * 2 + (0 if task == "test" else -1):03}'
        file_name = f'{actual_id}_{language_name}_{task}.json'
        convert_to_json(task + '.norm', os.path.join(data_path, language_name), os.path.join(output_path, "tasks"), file_name, actual_id)
        with open(os.path.join(output_path, f'splits/default/{task}_tasks.txt'), 'a') as out_file:
            out_file.write(file_name.split('.')[0] + '\n')


def err(msg):
    print('Error: ' + msg)
    exit(0)

if __name__ == '__main__':
    parser = OptionParser(description='Normalization baselines')
    parser.add_option("--data", help='path to the data normalization data')
    parser.add_option("--output", help='path to output data path')

    (opts, args) = parser.parse_args()
    if opts.data == None:
        err('Please provide data data with --data')
    if opts.output == None:
        err('Please provide data data with --output')
    
    if not os.path.exists(opts.output):
        os.makedirs(opts.output)
        os.makedirs(os.path.join(opts.output, 'tasks'))
        os.makedirs(os.path.join(opts.output, 'splits/default'))
    for lang_id, language_folder in enumerate(os.listdir(opts.data)):
        process_language_tasks(opts.data, opts.output, language_folder, lang_id + 1)

