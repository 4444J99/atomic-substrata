#!/usr/bin/env python3
"""
Advanced NLP Module
=================
Advanced natural language processing for atoms.

Features:
- Named Entity Recognition
- Sentiment Analysis
- Text Classification
- Keyword Extraction
- Summary Generation
"""

import re
from collections import Counter
from dataclasses import dataclass
from typing import Optional


try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer

    HAS_NLTK = True
except ImportError:
    HAS_NLTK = False


@dataclass
class Entity:
    """Represents a named entity."""

    text: str
    label: str
    start: int
    end: int


@dataclass
class SentimentResult:
    """Sentiment analysis result."""

    polarity: float  # -1 to 1
    sentiment: str  # positive, negative, neutral
    confidence: float


@dataclass
class ClassificationResult:
    """Text classification result."""

    category: str
    confidence: float


@dataclass
class KeywordResult:
    """Keyword extraction result."""

    keyword: str
    score: float


class AdvancedNLP:
    """Advanced NLP processing for atoms."""

    def __init__(self):
        self.sentiment_analyzer = None
        if HAS_NLTK:
            try:
                self.sentiment_analyzer = SentimentIntensityAnalyzer()
            except:
                pass

        # Common entity patterns
        self.entity_patterns = {
            "DATE": r"\b\d{4}-\d{2}-\d{2}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b",
            "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            "PHONE": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
            "VERSION": r"\bv?\d+\.\d+(?:\.\d+)?\b",
            "PATH": r"(?:[A-Za-z]:\\)?(?:[/\\][\w.-]+)+",
        }

    def extract_entities(self, text: str) -> list[Entity]:
        """
        Extract named entities from text.

        Args:
            text: Text to process

        Returns:
            List of entities
        """
        entities = []

        # Pattern-based entity extraction
        for label, pattern in self.entity_patterns.items():
            for match in re.finditer(pattern, text):
                entities.append(
                    Entity(
                        text=match.group(),
                        label=label,
                        start=match.start(),
                        end=match.end(),
                    )
                )

        # Capitalized phrase extraction (proper nouns)
        cap_pattern = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b")
        for match in cap_pattern.finditer(text):
            # Check if not already captured
            text_in_entities = any(e.text == match.group() for e in entities)
            if not text_in_entities:
                entities.append(
                    Entity(
                        text=match.group(),
                        label="PROPER_NOUN",
                        start=match.start(),
                        end=match.end(),
                    )
                )

        return entities

    def analyze_sentiment(self, text: str) -> SentimentResult:
        """
        Analyze sentiment of text.

        Args:
            text: Text to analyze

        Returns:
            SentimentResult
        """
        if self.sentiment_analyzer:
            scores = self.sentiment_analyzer.polarity_scores(text)
            polarity = scores["compound"]
        else:
            # Simple word-based sentiment
            polarity = self._simple_sentiment(text)

        if polarity > 0.05:
            sentiment = "positive"
        elif polarity < -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        confidence = abs(polarity)

        return SentimentResult(
            polarity=polarity, sentiment=sentiment, confidence=confidence
        )

    def _simple_sentiment(self, text: str) -> float:
        """Simple word-based sentiment analysis."""
        positive_words = {
            "good",
            "great",
            "excellent",
            "amazing",
            "wonderful",
            "fantastic",
            "love",
            "best",
            "perfect",
            "beautiful",
            "awesome",
            "nice",
            "happy",
            "success",
            "successful",
            "benefit",
            "useful",
            "helpful",
            "improve",
        }
        negative_words = {
            "bad",
            "terrible",
            "awful",
            "horrible",
            "worst",
            "hate",
            "poor",
            "fail",
            "failure",
            "error",
            "problem",
            "issue",
            "bug",
            "broken",
            "difficult",
            "hard",
            "complex",
            "confusing",
            "wrong",
        }

        text_lower = text.lower()
        words = re.findall(r"\b\w+\b", text_lower)

        pos_count = sum(1 for w in words if w in positive_words)
        neg_count = sum(1 for w in words if w in negative_words)

        total = pos_count + neg_count
        if total == 0:
            return 0.0

        return (pos_count - neg_count) / total

    def extract_keywords(self, text: str, top_k: int = 10) -> list[KeywordResult]:
        """
        Extract keywords from text.

        Args:
            text: Text to process
            top_k: Number of keywords to extract

        Returns:
            List of keywords with scores
        """
        # Simple TF-IDF-like keyword extraction
        words = re.findall(r"\b\w{3,}\b", text.lower())

        # Filter stopwords
        stopwords = {
            "the",
            "and",
            "for",
            "that",
            "this",
            "with",
            "from",
            "have",
            "has",
            "are",
            "were",
            "been",
            "being",
            "will",
            "would",
            "could",
            "should",
            "may",
            "might",
            "must",
            "shall",
            "can",
            "need",
            "dare",
            "ought",
            "used",
            "about",
            "after",
            "before",
            "more",
            "most",
            "some",
            "such",
            "only",
            "own",
            "same",
            "than",
            "too",
            "very",
            "just",
        }

        words = [w for w in words if w not in stopwords]

        # Count frequencies
        word_counts = Counter(words)
        total = sum(word_counts.values())

        # Score by frequency
        keywords = []
        for word, count in word_counts.most_common(top_k):
            score = count / total if total > 0 else 0
            keywords.append(KeywordResult(keyword=word, score=score))

        return keywords

    def classify_text(self, text: str) -> list[ClassificationResult]:
        """
        Classify text into categories.

        Args:
            text: Text to classify

        Returns:
            List of classification results
        """
        categories = {
            "technical": {
                "keywords": [
                    "api",
                    "function",
                    "class",
                    "method",
                    "code",
                    "algorithm",
                    "system",
                    "data",
                    "database",
                    "server",
                    "implementation",
                ],
                "weight": 1.0,
            },
            "scientific": {
                "keywords": [
                    "research",
                    "study",
                    "experiment",
                    "hypothesis",
                    "theory",
                    "analysis",
                    "data",
                    "results",
                    "evidence",
                ],
                "weight": 1.0,
            },
            "business": {
                "keywords": [
                    "market",
                    "customer",
                    "revenue",
                    "profit",
                    "strategy",
                    "product",
                    "sales",
                    "growth",
                    "company",
                ],
                "weight": 1.0,
            },
            "educational": {
                "keywords": [
                    "learn",
                    "teach",
                    "student",
                    "course",
                    "education",
                    "concept",
                    "explain",
                    "understand",
                ],
                "weight": 1.0,
            },
            "news": {
                "keywords": [
                    "announcement",
                    "report",
                    "update",
                    "new",
                    "latest",
                    "recent",
                    "today",
                    "yesterday",
                ],
                "weight": 1.0,
            },
        }

        text_lower = text.lower()
        results = []

        for category, info in categories.items():
            matches = sum(1 for kw in info["keywords"] if kw in text_lower)
            if matches > 0:
                confidence = min(matches * 0.2, 1.0)
                results.append(
                    ClassificationResult(category=category, confidence=confidence)
                )

        # Sort by confidence
        results.sort(key=lambda x: x.confidence, reverse=True)

        return results[:3]

    def summarize(self, text: str, max_sentences: int = 3) -> str:
        """
        Generate a simple extractive summary.

        Args:
            text: Text to summarize
            max_sentences: Maximum number of sentences

        Returns:
            Summary text
        """
        # Split into sentences
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) <= max_sentences:
            return text

        # Score sentences by keyword presence
        keywords = self.extract_keywords(text, top_k=15)
        keyword_set = {k.keyword for k in keywords}

        scored_sentences = []
        for sentence in sentences:
            words = set(re.findall(r"\b\w{3,}\b", sentence.lower()))
            score = len(words & keyword_set)
            scored_sentences.append((score, sentence))

        # Sort by score and take top
        scored_sentences.sort(key=lambda x: x[0], reverse=True)
        top_sentences = [s for _, s in scored_sentences[:max_sentences]]

        # Restore original order
        result_sentences = []
        for sentence in sentences:
            if sentence in top_sentences and sentence not in result_sentences:
                result_sentences.append(sentence)

        return ". ".join(result_sentences) + "."

    def analyze(self, text: str) -> dict:
        """
        Complete NLP analysis.

        Args:
            text: Text to analyze

        Returns:
            Dictionary with all analysis results
        """
        return {
            "entities": [
                {"text": e.text, "label": e.label} for e in self.extract_entities(text)
            ],
            "sentiment": {
                "polarity": self.analyze_sentiment(text).polarity,
                "sentiment": self.analyze_sentiment(text).sentiment,
            },
            "keywords": [
                {"keyword": k.keyword, "score": k.score}
                for k in self.extract_keywords(text)
            ],
            "classification": [
                {"category": c.category, "confidence": c.confidence}
                for c in self.classify_text(text)
            ],
            "summary": self.summarize(text),
        }


def main():
    """CLI for advanced NLP."""
    import sys

    nlp = AdvancedNLP()

    if len(sys.argv) < 2:
        print("Usage: advanced_nlp.py <command>")
        print("  entities <text>")
        print("  sentiment <text>")
        print("  keywords <text>")
        print("  classify <text>")
        print("  summarize <text>")
        print("  analyze <text>")
        return

    cmd = sys.argv[1]
    text = " ".join(sys.argv[2:])

    if cmd == "entities":
        entities = nlp.extract_entities(text)
        for e in entities:
            print(f"  {e.label}: {e.text}")

    elif cmd == "sentiment":
        result = nlp.analyze_sentiment(text)
        print(f"  Sentiment: {result.sentiment}")
        print(f"  Polarity: {result.polarity:.3f}")

    elif cmd == "keywords":
        keywords = nlp.extract_keywords(text)
        for k in keywords[:10]:
            print(f"  {k.keyword}: {k.score:.3f}")

    elif cmd == "classify":
        results = nlp.classify_text(text)
        for r in results:
            print(f"  {r.category}: {r.confidence:.3f}")

    elif cmd == "summarize":
        print(nlp.summarize(text))

    elif cmd == "analyze":
        import json

        print(json.dumps(nlp.analyze(text), indent=2))


if __name__ == "__main__":
    main()
