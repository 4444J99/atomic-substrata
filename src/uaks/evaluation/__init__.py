#!/usr/bin/env python3
"""
Evaluation Module
=================
Metrics and evaluation for UAKS atoms and assembly.

Features:
- Precision/recall metrics
- Similarity metrics
- Quality scoring
- Assembly evaluation
"""

import math
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EvaluationResult:
    """Result of an evaluation."""

    metric: str
    score: float
    details: dict = field(default_factory=dict)


class Evaluation:
    """Evaluation metrics for UAKS."""

    def __init__(self):
        pass

    def precision_at_k(
        self, relevant: list, retrieved: list, k: int = 10
    ) -> EvaluationResult:
        """
        Calculate precision at k.

        Args:
            relevant: List of relevant item IDs
            retrieved: List of retrieved item IDs
            k: Consider top k results

        Returns:
            Precision at k score
        """
        retrieved_k = retrieved[:k]
        relevant_set = set(relevant)

        num_relevant = sum(1 for item in retrieved_k if item in relevant_set)
        score = num_relevant / k if k > 0 else 0.0

        return EvaluationResult(
            metric="precision_at_k",
            score=score,
            details={"k": k, "relevant_found": num_relevant},
        )

    def recall_at_k(
        self, relevant: list, retrieved: list, k: int = 10
    ) -> EvaluationResult:
        """
        Calculate recall at k.

        Args:
            relevant: List of relevant item IDs
            retrieved: List of retrieved item IDs
            k: Consider top k results

        Returns:
            Recall at k score
        """
        retrieved_k = retrieved[:k]
        relevant_set = set(relevant)

        num_relevant = sum(1 for item in retrieved_k if item in relevant_set)
        score = num_relevant / len(relevant_set) if relevant_set else 0.0

        return EvaluationResult(
            metric="recall_at_k",
            score=score,
            details={
                "k": k,
                "relevant_found": num_relevant,
                "total_relevant": len(relevant_set),
            },
        )

    def f1_score(
        self, relevant: list, retrieved: list, k: int = 10
    ) -> EvaluationResult:
        """
        Calculate F1 score at k.

        Args:
            relevant: List of relevant item IDs
            retrieved: List of retrieved item IDs
            k: Consider top k results

        Returns:
            F1 score
        """
        precision = self.precision_at_k(relevant, retrieved, k)
        recall = self.recall_at_k(relevant, retrieved, k)

        if precision.score + recall.score == 0:
            score = 0.0
        else:
            score = (
                2 * (precision.score * recall.score) / (precision.score + recall.score)
            )

        return EvaluationResult(
            metric="f1_score",
            score=score,
            details={"precision": precision.score, "recall": recall.score},
        )

    def ndcg(self, relevant: list, retrieved: list, k: int = 10) -> EvaluationResult:
        """
        Calculate Normalized Discounted Cumulative Gain (NDCG).

        Args:
            relevant: List of relevant item IDs with relevance scores
            retrieved: List of retrieved item IDs
            k: Consider top k results

        Returns:
            NDCG score
        """
        retrieved_k = retrieved[:k]

        # Calculate DCG
        dcg = 0.0
        for i, item in enumerate(retrieved_k):
            rel = 0
            for r_item, r_score in relevant:
                if r_item == item:
                    rel = r_score
                    break
            dcg += rel / math.log2(i + 2)

        # Calculate IDCG
        idcg = 0.0
        sorted_relevant = sorted(relevant, key=lambda x: x[1], reverse=True)[:k]
        for i, (_, rel) in enumerate(sorted_relevant):
            idcg += rel / math.log2(i + 2)

        score = dcg / idcg if idcg > 0 else 0.0

        return EvaluationResult(
            metric="ndcg", score=score, details={"dcg": dcg, "idcg": idcg}
        )

    def mean_reciprocal_rank(self, relevant: list, retrieved: list) -> EvaluationResult:
        """
        Calculate Mean Reciprocal Rank (MRR).

        Args:
            relevant: List of relevant item IDs
            retrieved: List of retrieved item IDs

        Returns:
            MRR score
        """
        relevant_set = set(relevant)

        for i, item in enumerate(retrieved):
            if item in relevant_set:
                score = 1.0 / (i + 1)
                return EvaluationResult(
                    metric="mrr", score=score, details={"rank": i + 1}
                )

        return EvaluationResult(metric="mrr", score=0.0)

    def cosine_similarity(self, vec1: list[float], vec2: list[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        if not vec1 or not vec2:
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        mag1 = math.sqrt(sum(a * a for a in vec1))
        mag2 = math.sqrt(sum(b * b for b in vec2))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot_product / (mag1 * mag2)

    def jaccard_similarity(self, set1: set, set2: set) -> float:
        """Calculate Jaccard similarity between two sets."""
        if not set1 and not set2:
            return 1.0
        if not set1 or not set2:
            return 0.0

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0

    def text_quality_score(self, text: str) -> EvaluationResult:
        """
        Calculate text quality score.

        Args:
            text: Text to evaluate

        Returns:
            Quality score
        """
        words = text.split()

        # Basic metrics
        word_count = len(words)
        char_count = len(text)

        # Vocabulary richness
        unique_words = len(set(words))
        vocabulary_richness = unique_words / word_count if word_count > 0 else 0.0

        # Sentence complexity (average words per sentence)
        sentences = text.split(".")
        avg_sentence_length = word_count / len(sentences) if sentences else 0.0

        # Normalize scores
        vocabulary_score = min(vocabulary_richness * 2, 1.0)  # Cap at 1.0
        length_score = min(word_count / 100, 1.0)  # Ideal around 100 words

        # Combined score
        score = vocabulary_score * 0.4 + length_score * 0.6

        return EvaluationResult(
            metric="text_quality",
            score=score,
            details={
                "word_count": word_count,
                "unique_words": unique_words,
                "vocabulary_richness": vocabulary_richness,
                "avg_sentence_length": avg_sentence_length,
            },
        )


def main():
    """CLI for evaluation."""
    import sys

    eval = Evaluation()

    if len(sys.argv) < 3:
        print("Usage: evaluation.py <metric> <args>...")
        print("  precision relevant... --retrieved retrieved...")
        print("  text_quality <text>")
        return

    metric = sys.argv[1]

    if metric == "precision":
        relevant = sys.argv[2].split(",")
        retrieved = sys.argv[3].split(",") if "--retrieved" in sys.argv else []
        k = int(sys.argv[sys.argv.index("-k") + 1]) if "-k" in sys.argv else 10
        result = eval.precision_at_k(relevant, retrieved, k)
        print(f"Precision@{k}: {result.score:.4f}")

    elif metric == "text_quality":
        text = " ".join(sys.argv[2:])
        result = eval.text_quality_score(text)
        print(f"Text Quality: {result.score:.4f}")
        for key, value in result.details.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
