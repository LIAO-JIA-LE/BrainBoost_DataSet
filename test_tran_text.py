import json

# 將 JSON 資料集轉換為純文字
def convert_to_text(data):
    text_data = []
    text_data.append("[\n")
    for item in data:
        # 輸入 (input)
        count = 0
        instruction = item['input']
        text_data.append("{\n" + f"\"instruction\": \"{instruction}\",\n")
        text_data.append("\"input\": \"\",\n")
        text_data.append("\"output\": \"[\\n")
        # 輸出 (output)
        for output in item['output']:
            question = output['question']
            # print(question)
            level = output['level']
            tag = output['tag']
            if output.get('option') is not None:
                options = "\\\",\\n\\\"".join(output['option'])  # 將選項轉換為以逗號分隔的文字
            answer = output['answer']
            parse = output['parse']
            
            if count == 0:
                text_data.append("")
            # 將每個問題轉換為純文字，並加上換行符號 (\n)            
            text_data.append("{\\n" + f"\\\"question\\\": \\\"{question}\\\",\\n")
            text_data.append(f"\\\"level\\\": {level},\\n")
            text_data.append(f"\\\"tag\\\": \\\"{tag}\\\",\\n")
            if output.get('option') is not None:
                text_data.append(f"\\\"options\\\": \\n[\\n\\\"{options}\\\"\\n],\\n")
            text_data.append(f"\\\"answer\\\": \\\"{answer}\\\",\\n")
            text_data.append(f"\\\"parse\\\": \\\"{parse}\\\"\\n")  # 每個問題之間增加一個空行
            if count != len(item['output']) - 1:
                text_data.append("},\\n")
            else:
                text_data.append("}\\n]\"\n")
            count += 1
        text_data.append("},\n")
    text_data.pop()
    text_data.append("}\n]\n")
    # 將整個文本串聯起來，以 "\n" 分隔每一行
    return "".join(text_data)

# 讀取儲存好的純文字檔案並顯示內容
def read_and_convert_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # print("檔案內容如下：\n")
            # print(content)
        
        return convert_to_text(json.loads(content))
    except FileNotFoundError:
        print(f"檔案 '{file_path}' 未找到。請確認路徑是否正確。")
        
# def markdown_to_text(markdown_string):
#     """Converts a markdown string to plain text."""
#     html = markdown(markdown_string)
#     soup = BeautifulSoup(html, "html.parser")
#     text = soup.get_text()
#     return text

# 指定要讀取的檔案路徑
json_path = "test_1.json"

# 指定要讀取的檔案路徑
file_path = "fine_tuning_dataset.json"

# 轉換並輸出
text_output = read_and_convert_file(json_path)
# text_output = convert_to_text(data)

# 將結果保存到文件中（可選）
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text_output)

# 打印轉換後的純文字資料
# print(text_output)