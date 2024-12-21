import unittest
import runner_and_tournament 
import Runner as runner
from unittest import TestCase


class TournamentTest(TestCase): 
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():  #
            position = 1
            for key, value in test_value.items():
                position += 1

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_Begun_1(self):
        Begun_1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = Begun_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_Begun_2(self):
        Begun_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = Begun_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_Begun_3(self):
        Begun_3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = Begun_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')


TournamentTest()


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = runner.Runner('1')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner.Runner('1')
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_1.run()
        for i in range(10):
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


RunnerTest()