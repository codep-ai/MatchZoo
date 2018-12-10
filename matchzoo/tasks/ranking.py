"""Ranking task."""

from matchzoo import engine


class Ranking(engine.BaseTask):
    """Ranking Task.

    Examples:
        >>> ranking_task = Ranking()
        >>> ranking_task.metrics = ['map', 'ndcg']
        >>> ranking_task.output_shape
        (1,)
        >>> ranking_task.output_dtype
        <class 'float'>
        >>> print(ranking_task)
        Ranking task

    """

    @classmethod
    def list_available_losses(cls) -> list:
        """:return: a list of available losses."""
        return ['mse']

    @classmethod
    def list_available_metrics(cls) -> list:
        """:return: a list of available metrics."""
        return ['mae']

    @property
    def output_shape(self) -> tuple:
        """:return: output shape of a single sample of the task."""
        return 1,

    @property
    def output_dtype(self):
        """:return: target data type, expect `float` as output."""
        return float

    def __str__(self):
        """:return: Task name as string."""
        return 'Ranking Task'
