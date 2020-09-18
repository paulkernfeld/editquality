from editquality.bwds import import_from_path, cache_parse, Edit, Bot, read_rev_pages
from editquality.utilities.bad_words_detection_system import bot_gen


EDITS = [Edit(1, {'one': 1, 'two': 2}, False), Edit(2, {'three': 3}, True), Edit(3, {'one': 5, 'four': 1}, False)]


def test_import_from_path():
    import_from_path('revscoring.languages.english')


def test_cache_parse():
    cache_parse(
        'editquality/bwds/tests/words_db.txt,'
        'editquality/bwds/tests/bad_edits_words.txt,'
        'editquality/bwds/tests/no_docs.txt',
        0
    )


def test_bot_gen():
    en_main_page_id = 232335
    a_revision_id = 7101436
    en_api_url = 'https://en.wikipedia.org/w/api.php'
    bot_gen([(en_main_page_id, a_revision_id)], 'TODO', en_api_url)


def test_read_rev_pages():
    assert list(read_rev_pages(["0", "1\t2"])) == [(0, None), (1, 2)]


def test_parse_bad_edits():
    bot = Bot()
    bot.parse_edits(EDITS)
    bot.parse_bad_edits(numbers_to_show=0)


def dump_empty():
    bot = Bot()
    bot.dump()
    with open('words_db.txt') as words_db:
        assert words_db.read() == '{}'
    with open('bad_edits_words.txt') as bad_edits_words:
        assert bad_edits_words.read() == '{}'
    with open('no_docs.txt') as no_docs:
        assert no_docs.read() == '0'


def dump_toy_data():
    bot = Bot()
    bot.parse_edits(EDITS)
    bot.parse_bad_edits(0)
    bot.dump()
    with open('words_db.txt') as words_db:
        assert words_db.read() == '{"three": 1}'
    with open('bad_edits_words.txt') as bad_edits_words:
        assert bad_edits_words.read() == '{"three": 3}'
    with open('no_docs.txt') as no_docs:
        assert no_docs.read() == '4'


def test_dump():
    # Calling both tests from here because we want to ensure they're not run concurrently
    dump_empty()
    dump_toy_data()
