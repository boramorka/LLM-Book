import os
import shutil

SRC_ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs')
SRC_ROOT = os.path.abspath(SRC_ROOT)
RU_ROOT = os.path.join(SRC_ROOT, 'ru')

# Map English filenames to Russian filenames
FILENAME_MAP = {
    'index.md': 'index.md',
    '1.1 Introduction.md': '1.1 Введение.md',
    '1.2 Classification.md': '1.2 Классификация.md',
    '1.3 Advanced Moderaton.md': '1.3 Advanced Moderaton.md',
    '1.4 Elevating Machine Reasoning: Advanced Strategies.md': '1.4 Продвинутое машинное рассуждение.md',
    '1.5 The Power of Prompt Chaining.md': '1.5 Сила чейнинга промптов.md',
    '1.6 Building and Evaluating LLM Applications.md': '1.6 Построение и оценка LLM-приложений.md',
    '1.7 Summary and Reflections.md': '1.7 Итоги и размышления.md',
    '2.1 Introduction.md': '2.1 Введение.md',
    '2.2 LangChain Document Loaders.md': '2.2 Загрузчики документов LangChain.md',
    '2.3 Deep Dive into Text Splitting.md': '2.3 Углубление в текстовое разбиение.md',
    '2.4 The Power of Embeddings.md': '2.4 Сила эмбеддингов.md',
    '2.5 Semantic Search. Advanced Retrieval Strategies.md': '2.5 Семантический поиск. Продвинутые стратегии.md',
    '2.6 RAG Systems. Techniques for Question Answering.md': '2.6 RAG. Техники для QA.md',
    '2.7 Building Chatbots with LangChain.md': '2.7 Чат-боты на LangChain.md',
    '2.8 Summary and Reflections.md': '2.8 Итоги и размышления.md',
    '3.1 Introduction.md': '3.1 Введение.md',
    '3.2 Mastering LLM Workflows with Kubeflow Pipelines.md': '3.2 Воркфлоу с Kubeflow Pipelines.md',
    '3.3 Implementing the AI Quiz Generation Mechanism.md': '3.3 Механизм генерации квиза ИИ.md',
    '3.4 Summary and Reflections.md': '3.4 Итоги и размышления.md',
    'Answers 1.1.md': 'Ответы 1.1.md',
    'Answers 1.2.md': 'Ответы 1.2.md',
    'Answers 1.3.md': 'Ответы 1.3.md',
    'Answers 1.4.md': 'Ответы 1.4.md',
    'Answers 1.5.md': 'Ответы 1.5.md',
    'Answers 1.6.md': 'Ответы 1.6.md',
    'Answers 2.2.md': 'Ответы 2.2.md',
    'Answers 2.3.md': 'Ответы 2.3.md',
    'Answers 2.4.md': 'Ответы 2.4.md',
    'Answers 2.5.md': 'Ответы 2.5.md',
    'Answers 2.6.md': 'Ответы 2.6.md',
    'Answers 2.7.md': 'Ответы 2.7.md',
    'Answers 3.2.md': 'Ответы 3.2.md',
    'Answers 3.3.md': 'Ответы 3.3.md',
}

def ensure_dir(path: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

def copy_tree_en_to_ru() -> None:
    ensure_dir(RU_ROOT)
    for chapter in os.listdir(SRC_ROOT):
        src_chapter_dir = os.path.join(SRC_ROOT, chapter)
        if chapter == 'ru' or not os.path.isdir(src_chapter_dir):
            continue
        ru_chapter_dir = os.path.join(RU_ROOT, chapter)
        ensure_dir(ru_chapter_dir)
        for name in os.listdir(src_chapter_dir):
            if not name.endswith('.md'):
                continue
            src_file = os.path.join(src_chapter_dir, name)
            ru_name = FILENAME_MAP.get(name, name)
            dst_file = os.path.join(ru_chapter_dir, ru_name)
            ensure_dir(os.path.dirname(dst_file))
            shutil.copy2(src_file, dst_file)

    # Top-level index.md
    src_index = os.path.join(SRC_ROOT, 'index.md')
    if os.path.isfile(src_index):
        shutil.copy2(src_index, os.path.join(RU_ROOT, 'index.md'))

if __name__ == '__main__':
    copy_tree_en_to_ru()
    print('docs/ru populated with copies (filenames localized).')


