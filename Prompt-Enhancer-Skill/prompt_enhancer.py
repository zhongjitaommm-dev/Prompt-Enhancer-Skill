def enhance_prompt(short_prompt):
    return f"""
优化后的AI提示词：

你是一名专业领域专家，
请围绕“{short_prompt}”完成任务。

要求：
1. 明确任务目标；
2. 补充背景信息；
3. 增加具体要求和限制条件；
4. 给出清晰输出格式。
"""

if __name__ == "__main__":
    text = input("请输入简短提示词：")
    print(enhance_prompt(text))
