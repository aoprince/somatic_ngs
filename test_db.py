import csv

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse


Base = declarative_base()

class Sample(Base):
    __tablename__ = "samples"

    sample_id = Column("sample_id", Integer, primary_key=True)

    def __init__(self, sample_id):
        self.sample_id = sample_id

    def __repr__(self):
        return f"({self.sample_id})"
    

class Sample_run(Base):
    __tablename__ = "sample_run"

    sample_run_id = Column("sample_run_id", Integer, primary_key=True)
    run_id = Column("run_id", Integer)
    sample_id = Column(Integer, ForeignKey("samples.sample_id"))

    def __init__(self, sample_run_id, run_id, sample_id):
        self.sample_run_id = sample_run_id
        self.run_id = run_id
        self.sample_id = sample_id

    def __repr__(self):
        return f"({self.sample_run_id} {self.run_id} {self.sample_id})"

class Run_table(Base):
    __tablename__ = "run_table"

    run_id = Column("run_id", Integer, primary_key=True)
    run_name = Column("run_name", String)
    date_of_test = Column("date_of_test", Integer)

    def __init__(self, run_id, run_name, date_of_test):
        self.run_id = run_id
        self.run_name = run_name
        self.date_of_test = date_of_test

    def __repr__(self):
        return f"({self.run_id} {self.run_name} {self.date_of_test})"

class Quality_files(Base):
    __tablename__ = "quality_files"

    quality_files_id = Column("quality_files_id", Integer, primary_key=True)
    sample_run_id = Column(Integer, ForeignKey("sample_run.sample_run_id"))
    Picard_HsMetrics_id = Column(Integer, ForeignKey("Picard_HsMetrics.Picard_HsMetrics_id"))
    samtools_flagstat_id = Column(Integer, ForeignKey("samtools_flagstat.samtools_flagstat_id"))
    Picard_markduplicates_id = Column(Integer, ForeignKey("Picard_markduplicates.Picard_markduplicates_id"))
    FastQC_id = Column(Integer, ForeignKey("FastQC.FastQC_id"))

    def __init__(self, quality_files_id, sample_run_id, Picard_HsMetrics_id, samtools_flagstat_id, Picard_markduplicates_id, FastQC_id):
        self.quality_files_id = quality_files_id
        self.sample_run_id = sample_run_id
        self.Picard_HsMetrics_id = Picard_HsMetrics_id
        self.samtools_flagstat_id = samtools_flagstat_id
        self.Picard_markduplicates_id = Picard_markduplicates_id
        self.FastQC_id = FastQC_id

    def __repr__(self):
        return f"({self.quality_files_id} {self.sample_run_id} {self.Picard_HsMetrics_id} {self.samtools_flagstat_id} {self.Picard_markduplicates_id} {self.FastQC_id})"

class Picard_HsMetrics(Base):
    __tablename__ = "Picard_HsMetrics"

    Picard_HsMetrics_id = Column("Picard_HsMetrics_id", Integer, primary_key=True)
    BAIT_SET = Column("BAIT_SET", Float)
    BAIT_TERRITORY = Column("BAIT_TERITORY", Float)
    BAIT_DESIGN_EFFICIENCY = Column("BAIT_DESIGN_EFFICIENCY", Float)
    ON_BAIT_BASES = Column("ON_BAIT_BASES", Float) 
    NEAR_BAIT_BASES = Column("NEAR_BAIT_BASES", Float)
    OFF_BAIT_BASES = Column("OFF_BAIT_BASES", Float)
    PCT_OFF_BAIT = Column("PCT_OFF_BAIT", Float)
    ON_BAIT_VS_SELECTED = Column("ON_BAIT_VS_SELECTED", Float)
    MEAN_BAIT_COVERAGE = Column("MEAN_BAIT_COVERAGE", Float)
    PCT_USABLE_BASES_ON_BAIT = Column("PCT_USABLE_BASES_ON_BAIT", Float)
    PCT_USABLE_BASES_ON_TARGET = Column("PCT_USABLE_BASES_ON_TARGET", Float)
    FOLD_ENRICHMENT = Column("FOLD_ENRICHMENT", Float)
    HS_LIBRARY_SIZE = Column("HS_LIBRARY_SIZE", Float)
    HS_PENALTY_10X = Column("HS_PENALTY_10X", Float)
    HS_PENALTY_20X = Column("HS_PENALTY_20X", Float)
    HS_PENALTY_30X = Column("HS_PENALTY_30X", Float)
    HS_PENALTY_40X = Column("HS_PENALTY_40X", Float)
    HS_PENALTY_50X = Column("HS_PENALTY_50X", Float)
    HS_PENALTY_100X = Column("HS_PENALTY_100X", Float)
    TARGET_TERRITORY = Column("TARGET_TERRITORY", Float)
    GENOME_SIZE = Column("GENOME_SIZE", Float)
    TOTAL_READS = Column("TOTAL_READS", Float)
    PF_READS = Column("PF_READS", Float)
    PF_BASES = Column("PF_BASES", Float)
    PF_UNIQUE_READS = Column("PF_UNIQUE_READS", Float)
    PF_UQ_READS_ALIGNED = Column("PF_UQ_READS_ALIGNED", Float)
    PF_BASES_ALIGNED = Column("PF_BASES_ALIGNED", Float)
    PF_UQ_BASES_ALIGNED = Column("PF_UQ_BASES_ALIGNED", Float)
    MEAN_TARGET_COVERAGE = Column("MEAN_TARGET_COVERAGE", Float)
    MEDIAN_TARGET_COVERAGE = Column("MEDIAN_TARGET_COVERAGE", Float)
    MAX_TARGET_COVERAGE = Column("MAX_TARGET_COVERAGE", Float)
    MIN_TARGET_COVERAGE = Column("MIN_TARGET_COVERAGE", Float)
    ZERO_CVG_TARGETS_PCT = Column("ZERO_CVG_TARGETS_PCT", Float)
    PCT_EXC_DUPE = Column("PCT_EXC_DUPE", Float)
    PCT_EXC_ADPATER = Column("PCT_EXC_ADAPTER", Float)
    PCT_EXC_MAPQ = Column("PCT_EXC_MAPQ", Float)
    PCT_EXC_BASEQ = Column("PCT_EXC_BASEQ", Float)
    PCT_EXC_OVERLAP = Column("PCT_EXC_OVERLAP", Float)
    PCT_EXC_OFF_TARGET = Column("PCT_EXC_OFF_TARGET", Float)
    FOLD_80_BASE_PENALTY = Column("FOLD_80_BASE_PENALTY", Float)
    PCT_TARGET_BASES_1X = Column("PCT_TARGET_BASES_1X", Float)
    PCT_TARGET_BASES_2X = Column("PCT_TARGET_BASES_2X", Float)
    PCT_TARGET_BASES_10X = Column("PCT_TARGET_BASES_10X", Float)
    PCT_TARGET_BASES_20X = Column("PCT_TARGET_BASES_20X", Float)
    PCT_TARGET_BASES_30X = Column("PCT_TARGET_BASES_30X", Float)
    PCT_TARGET_BASES_40X = Column("PCT_TARGET_BASES_40X", Float)
    PCT_TARGET_BASES_50X = Column("PCT_TARGET_BASES_50X", Float)
    PCT_TARGET_BASES_100X = Column("PCT_TARGET_BASES_100X", Float)
    AT_DROPOUT = Column("AT_DROPOUT", Float)
    GC_DROPOUT = Column("GC_DROPOUT", Float)
    HET_SNP_SENSITIVITY = Column("HET_SNP_SENSITIVITY", Float)
    HET_SNP_Q = Column("HET_SNP_Q", Float)
    SAMPLE_LIBRARY_READ_GROUP = Column("SAMPLE_LIBRARY_READ_GROUP", Float)

    def __init__(self, Picard_HsMetrics_id, BAIT_SET, BAIT_TERRITORY, BAIT_DESIGN_EFFICIENCY, ON_BAIT_BASES, NEAR_BAIT_BASES, OFF_BAIT_BASES, PCT_OFF_BAIT, \
                 ON_BAIT_VS_SELECTED, MEAN_BAIT_COVERAGE, PCT_USABLE_BASES_ON_BAIT, PCT_USABLE_BASES_ON_TARGET, FOLD_ENRICHMENT, HS_LIBRARY_SIZE, HS_PENALTY_10X, \
                 HS_PENALTY_20X, HS_PENALTY_30X, HS_PENALTY_40X, HS_PENALTY_50X, HS_PENALTY_100X, TARGET_TERRITORY, GENOME_SIZE, TOTAL_READS, PF_READS, PF_BASES, PF_UNIQUE_READS, \
                 PF_UQ_READS_ALIGNED, PF_BASES_ALIGNED, PF_UQ_BASES_ALIGNED, MEAN_TARGET_COVERAGE, MEDIAN_TARGET_COVERAGE, MAX_TARGET_COVERAGE, MIN_TARGET_COVERAGE, \
                 ZERO_CVG_TARGETS_PCT, PCT_EXC_DUPE, PCT_EXC_ADPATER, PCT_EXC_MAPQ, PCT_EXC_BASEQ, PCT_EXC_OVERLAP, PCT_EXC_OFF_TARGET, FOLD_80_BASE_PENALTY, PCT_TARGET_BASES_1X, \
                 PCT_TARGET_BASES_2X, PCT_TARGET_BASES_10X, PCT_TARGET_BASES_20X, PCT_TARGET_BASES_30X, PCT_TARGET_BASES_40X, PCT_TARGET_BASES_50X, PCT_TARGET_BASES_100X, AT_DROPOUT, \
                 GC_DROPOUT, HET_SNP_SENSITIVITY, HET_SNP_Q, SAMPLE_LIBRARY_READ_GROUP):
        self.Picard_HsMetrics_id = Picard_HsMetrics_id
        self.BAIT_SET = BAIT_SET
        self.BAIT_TERRITORY = BAIT_TERRITORY
        self.BAIT_DESIGN_EFFICIENCY = BAIT_DESIGN_EFFICIENCY
        self.ON_BAIT_BASES = ON_BAIT_BASES
        self.NEAR_BAIT_BASES = NEAR_BAIT_BASES
        self.OFF_BAIT_BASES = OFF_BAIT_BASES
        self.PCT_OFF_BAIT = PCT_OFF_BAIT
        self.ON_BAIT_VS_SELECTED = ON_BAIT_VS_SELECTED
        self.MEAN_BAIT_COVERAGE = MEAN_BAIT_COVERAGE
        self.PCT_USABLE_BASES_ON_BAIT = PCT_USABLE_BASES_ON_BAIT
        self.PCT_USABLE_BASES_ON_TARGET = PCT_USABLE_BASES_ON_TARGET
        self.FOLD_ENRICHMENT = FOLD_ENRICHMENT
        self.HS_LIBRARY_SIZE = HS_LIBRARY_SIZE
        self.HS_PENALTY_10X = HS_PENALTY_10X
        self.HS_PENALTY_20X = HS_PENALTY_20X
        self.HS_PENALTY_30X = HS_PENALTY_30X
        self.HS_PENALTY_40X = HS_PENALTY_40X
        self.HS_PENALTY_50X = HS_PENALTY_50X
        self.HS_PENALTY_100X = HS_PENALTY_100X
        self.TARGET_TERRITORY = TARGET_TERRITORY
        self.GENOME_SIZE = GENOME_SIZE
        self.TOTAL_READS = TOTAL_READS
        self.PF_READS = PF_READS
        self.PF_BASES = PF_BASES
        self.PF_UNIQUE_READS = PF_UNIQUE_READS
        self.PF_UQ_READS_ALIGNED = PF_UQ_READS_ALIGNED
        self.PF_BASES_ALIGNED = PF_BASES_ALIGNED
        self.PF_UQ_BASES_ALIGNED = PF_UQ_BASES_ALIGNED
        self.MEAN_TARGET_COVERAGE = MEAN_TARGET_COVERAGE
        self.MEDIAN_TARGET_COVERAGE = MEDIAN_TARGET_COVERAGE
        self.MAX_TARGET_COVERAGE = MAX_TARGET_COVERAGE
        self.MIN_TARGET_COVERAGE = MIN_TARGET_COVERAGE
        self.ZERO_CVG_TARGETS_PCT = ZERO_CVG_TARGETS_PCT
        self.PCT_EXC_DUPE = PCT_EXC_DUPE
        self.PCT_EXC_ADPATER = PCT_EXC_ADPATER
        self.PCT_EXC_MAPQ = PCT_EXC_MAPQ
        self.PCT_EXC_BASEQ = PCT_EXC_BASEQ
        self.PCT_EXC_OVERLAP = PCT_EXC_OVERLAP
        self.PCT_EXC_OFF_TARGET = PCT_EXC_OFF_TARGET
        self.FOLD_80_BASE_PENALTY = FOLD_80_BASE_PENALTY
        self.PCT_TARGET_BASES_1X = PCT_TARGET_BASES_1X
        self.PCT_TARGET_BASES_2X = PCT_TARGET_BASES_2X
        self.PCT_TARGET_BASES_10X = PCT_TARGET_BASES_10X
        self.PCT_TARGET_BASES_20X = PCT_TARGET_BASES_20X
        self.PCT_TARGET_BASES_30X = PCT_TARGET_BASES_30X
        self.PCT_TARGET_BASES_40X = PCT_TARGET_BASES_40X
        self.PCT_TARGET_BASES_50X = PCT_TARGET_BASES_50X
        self.PCT_TARGET_BASES_100X = PCT_TARGET_BASES_100X
        self.AT_DROPOUT = AT_DROPOUT
        self.GC_DROPOUT = GC_DROPOUT
        self.HET_SNP_SENSITIVITY = HET_SNP_SENSITIVITY
        self.HET_SNP_Q = HET_SNP_Q
        self.SAMPLE_LIBRARY_READ_GROUP = SAMPLE_LIBRARY_READ_GROUP

    def __repr__(self):
        return f"({self.Picard_HsMetrics_id} {self.BAIT_SET} {self.BAIT_TERRITORY} {self.BAIT_DESIGN_EFFICIENCY} {self.ON_BAIT_BASES} {self.NEAR_BAIT_BASES} \
        {self.OFF_BAIT_BASES} {self.PCT_OFF_BAIT} {self.ON_BAIT_VS_SELECTED} {self.MEAN_BAIT_COVERAGE} {self.PCT_USABLE_BASES_ON_BAIT} {self.PCT_USABLE_BASES_ON_TARGET} \
        {self.FOLD_ENRICHMENT} {self.HS_LIBRARY_SIZE} {self.HS_PENALTY_10X} {self.HS_PENALTY_20X} {self.HS_PENALTY_30X} {self.HS_PENALTY_40X} {self.HS_PENALTY_50X} \
        {self.HS_PENALTY_100X} {self.TARGET_TERRITORY} {self.GENOME_SIZE} {self.TOTAL_READS} {self.PF_READS} {self.PF_BASES} {self.PF_UNIQUE_READS} {self.PF_UQ_READS_ALIGNED} \
        {self.PF_BASES_ALIGNED} {self.MEAN_TARGET_COVERAGE} {self.MEDIAN_TARGET_COVERAGE} {self.MAX_TARGET_COVERAGE} {self.MIN_TARGET_COVERAGE} {self.ZERO_CVG_TARGETS_PCT} \
        {self.PCT_EXC_DUPE} {self.PCT_EXC_ADPATER} {self.PCT_EXC_MAPQ} {self.PCT_EXC_BASEQ} {self.PCT_EXC_OVERLAP} {self.PCT_EXC_OFF_TARGET} {self.FOLD_80_BASE_PENALTY} \
        {self.PCT_TARGET_BASES_1X} {self.PCT_TARGET_BASES_2X} {self.PCT_TARGET_BASES_10X} {self.PCT_TARGET_BASES_20X} {self.PCT_TARGET_BASES_30X} {self.PCT_TARGET_BASES_40X} \
        {self.PCT_TARGET_BASES_50X} {self.PCT_TARGET_BASES_100X} {self.AT_DROPOUT} {self.GC_DROPOUT} {self.HET_SNP_SENSITIVITY} {self.HET_SNP_Q} {self.SAMPLE_LIBRARY_READ_GROUP}"


class samtools_flagstat(Base):
    __tablename__ = "samtools_flagstat"

    samtools_flagstat_id = Column("samtools_flagstat_id", Integer, primary_key=True)
    total_passed = Column("total_passed", Integer)
    total_failed = Column("total_failed", Integer)
    secondary_passed = Column("secondary_passed", Integer)
    secondary_failed = Column("secondary_failed", Integer)
    supplementary_passed = Column("supplementary_passed", Integer)
    supplementary_failed = Column("supplementary_failed", Integer)
    duplicates_passed = Column("duplicates_passed", Integer)
    duplicates_failed = Column("duplicates_failed", Integer)
    mapped_passed = Column("mapped_passed", Integer)
    mapped_failed = Column("mapped_failed", Integer)
    mapped_passed_pct = Column("mapped_passed_pct", Integer)
    mapped_failed_pct = Column("mapped_failed_pct", Integer)
    paired_in_sequencing_passed = Column("paired_in_sequencing_passed", Integer)
    paired_in_sequencing_failed = Column("paired_in_sequencing_failed", Integer)
    read1_passed = Column("read1_passed", Integer)
    read1_failed = Column("read1_failed", Integer)
    read2_passed = Column("read2_passed", Integer)
    read2_failed = Column("read2_failed", Integer)
    properly_paired_passed = Column("properly_paired_passed", Integer)
    properly_paired_failed = Column("properly_paired_failed", Integer)
    properly_paired_passed_pct = Column("properly_paired_passed_pct", Integer)
    properly_paired_failed_pct = Column("properly_paired_failed_pct", Integer)
    with_itself_and_mate_mapped_passed = Column("with_itself_and_mate_mapped_passed", Integer)
    with_itself_and_mate_mapped_failed = Column("with_itself_and_mate_mapped_failed", Integer)
    singletons_passed = Column("singletons_passed", Integer)
    singletons_failed = Column("singletons_failed", Integer)
    singletons_passed_pct = Column("singletons_passed", Integer)
    singletons_failed_pct = Column("singletons_failure_pct", Integer)
    with_mate_mapped_to_a_different_chr_passed = Column("with_mate_mapped_to_a_different_chr_passed", Integer)
    with_mate_mapped_to_a_different_chr_failed = Column("with_mate_mapped_to_a_different_chr_failed", Integer)
    with_mate_mapped_to_a_different_chr_mapQ5_passed = Column("with_mate_mapped_to_a_different_chr_passed", Integer)
    with_mate_mapped_to_a_different_chr_mapQ5_failed = Column("with_mate_mapped_to_a_different_chr_failed", Integer)
    flagstat_total = Column("flagstat_total", Integer)

    def __init__(self, samtools_flagstat_id, total_passed, total_failed, secondary_passed, secondary_failed, supplementary_passed, supplementary_failed, \
                 duplicates_passed, duplicates_failed, mapped_passed, mapped_failed, mapped_passed_pct, mapped_failed_pct, paired_in_sequencing_passed, paired_in_sequencing_failed, \
                 read1_passed, read1_failed, read2_passed, read2_failed, properly_paired_passed, properly_paired_failed, properly_paired_passed_pct, properly_paired_failed_pct, \
                 with_itself_and_mate_mapped_passed, with_itself_and_mate_mapped_failed, singeltons_passed, singeltons_failed, singeltons_passed_pct, singletons_failed_pct, \
                 with_mate_mapped_to_a_different_chr_passed, with_mate_mapped_to_a_different_chr_failed, with_mate_mapped_to_a_different_chr_mapQ5_passed, \
                 with_mate_mapped_to_a_different_chr_mapQ5_failed, flagstat_total):
        self.samtools_flagstat_id = samtools_flagstat_id
        self.total_passed = total_passed
        self.total_failed = total_failed
        self.secondary_passed = secondary_passed
        self.secondary_failed = secondary_failed
        self.supplementary_passed = supplementary_passed
        self.supplementary_failed = supplementary_failed
        self.duplicates_passed = duplicates_passed
        self.duplicates_failed = duplicates_failed
        self.mapped_passed = mapped_passed
        self.mapped_failed = mapped_failed
        self.mapped_passed_pct = mapped_passed_pct
        self.mapped_failed_pct = mapped_failed_pct
        self.paired_in_sequencing_passed = paired_in_sequencing_passed
        self.paired_in_sequencing_failed = paired_in_sequencing_failed
        self.read1_passed = read1_passed
        self.read1_failed = read1_failed
        self.read2_passed = read2_passed
        self.read2_failed = read2_failed
        self.properly_paired_passed = properly_paired_passed
        self.properly_paired_failed = properly_paired_failed
        self.properly_paired_passed_pct = properly_paired_passed_pct
        self.properly_paired_failed_pct = properly_paired_failed_pct
        self.with_itself_and_mate_mapped_passed = with_itself_and_mate_mapped_passed
        self.with_itself_and_mate_mapped_failed = with_itself_and_mate_mapped_failed
        self.singletons_passed = singeltons_passed
        self.singletons_failed = singeltons_failed
        self.singletons_passed_pct = singeltons_passed_pct
        self.singletons_failed_pct = singletons_failed_pct
        self.with_mate_mapped_to_a_different_chr_passed = with_mate_mapped_to_a_different_chr_passed
        self.with_mate_mapped_to_a_different_chr_failed = with_mate_mapped_to_a_different_chr_failed
        self.with_mate_mapped_to_a_different_chr_mapQ5_passed = with_mate_mapped_to_a_different_chr_mapQ5_passed
        self.with_mate_mapped_to_a_different_chr_mapQ5_failed = with_mate_mapped_to_a_different_chr_mapQ5_failed
        self.flagstat_total = flagstat_total


    def __repr__(self):
         return f"({self.samtools_flagstat_id} {self.total_passed} {self.total_failed} {self.secondary_passed} {self.secondary_failed} {self.supplementary_passed} \
         {self.supplementary_failed} {self.duplicates_passed} {self.duplicates_failed} {self.mapped_passed} {self.mapped_failed} {self.mapped_passed_pct} \
         {self.mapped_failed_pct} {self.paired_in_sequencing_passed} {self.paired_in_sequencing_failed} {self.read1_passed} {self.read1_failed} {self.read2_passed} \
         {self.read2_failed} {self.properly_paired_passed} {self.properly_paired_failed} {self.properly_paired_passed_pct} {self.properly_paired_failed_pct} \
         {self.with_itself_and_mate_mapped_passed} {self.with_itself_and_mate_mapped_failed} {self.singletons_passed} {self.singletons_failed} {self.singletons_passed_pct} \
         {self.singletons_failed_pct} {self.with_mate_mapped_to_a_different_chr_passed} {self.with_mate_mapped_to_a_different_chr_failed} \
         {self.with_mate_mapped_to_a_different_chr_mapQ5_passed} {self.with_mate_mapped_to_a_different_chr_mapQ5_failed} {self.flagstat_total}"



class Picard_markduplicates(Base):
    __tablename__ = "Picard_markduplicates"

    Picard_markduplicates_id = Column("Picard_markduplicates_id", Integer, primary_key=True)
    LIBRARY = Column("LIBRARY", Integer)
    UNPAIRED_READS_EXAMINED = Column("UNPAIRED_READS_EXAMINED", Integer)
    READ_PAIRS_EXAMINED = Column("READ_PAIRS_EXAMINED", Integer)
    SECONDARY_OR_SUPPLEMENTARY_RDS = Column("SECONDARY_OR_SUPPLEMENTARY_RDS", Integer)
    UNMAPPED_READS = Column("UNMAPPED_READS", Integer)
    UNPAIRED_READ_DUPLICATES = Column("UNPAIRED_READ_DUPLICATES", Integer)
    READ_PAIR_DUPLICATES = Column("READ_PAIR_DUPLICATES", Integer)
    READ_PAIR_OPTICAL_DUPLICATES = Column("READ_PAIR__OPTICAL_DUPLICATES", Integer)
    PERCENT_DUPLICATION = Column("PERCENT_DUPLICATION", Integer)
    ESTIMATED_LIBRARY_SIZE = Column("ESTIMATED_LIBRARY_SIZE", Integer)


    def __init__(self, Picard_markduplicates_id, LIBRARY, UNPAIRED_READS_EXAMINED, READ_PAIRS_EXAMINED, SECONDARY_OR_SUPPLEMENTARY, UNMAPPED_READS, \
                 UNPAIRED_READ_DUPLICATES, READ_PAIR_DUPLICATES, READ_PAIR_OPTICAL_DUPLICATES, PERCENT_DUPLICATION, ESTIMATED_LIBRARY_SIZE):
        self.Picard_markduplicates_id = Picard_markduplicates_id
        self.LIBRARY = LIBRARY
        self.UNPAIRED_READS_EXAMINED = UNPAIRED_READS_EXAMINED
        self.READ_PAIRS_EXAMINED = READ_PAIRS_EXAMINED
        self.SECONDARY_OR_SUPPLEMENTARY_RDS = SECONDARY_OR_SUPPLEMENTARY
        self.UNMAPPED_READS = UNMAPPED_READS
        self.UNPAIRED_READ_DUPLICATES = UNPAIRED_READ_DUPLICATES
        self.READ_PAIR_DUPLICATES = READ_PAIR_DUPLICATES
        self.READ_PAIR_OPTICAL_DUPLICATES = READ_PAIR_OPTICAL_DUPLICATES
        self.PERCENT_DUPLICATION = PERCENT_DUPLICATION
        self.ESTIMATED_LIBRARY_SIZE = ESTIMATED_LIBRARY_SIZE

    def __repr__(self):
        return f"({self.Picard_markduplicates_id} {self.LIBRARY} {self.UNPAIRED_READS_EXAMINED} {self.READ_PAIRS_EXAMINED} {self.SECONDARY_OR_SUPPLEMENTARY_RDS} \
        {self.UNMAPPED_READS} {self.UNPAIRED_READ_DUPLICATES} {self.READ_PAIR_DUPLICATES} {self.READ_PAIR_OPTICAL_DUPLICATES} {self.PERCENT_DUPLICATION} \
        {self.ESTIMATED_LIBRARY_SIZE}" 




class FastQC(Base):
    __tablename__ = "FastQC"

    FastQC_id = Column("FastQC_id", Integer, primary_key=True)
    Filename = Column("Filename", String)
    File_type = Column("File_type", String)
    Encoding = Column("Encoding", String)
    Total_Sequences = Column("Total_Sequences", Float)
    Sequences_flagged_as_poor_quality = Column("Sequences_flagged_as_poor_quality", Integer)
    Sequence_length = Column("Sequence_length", Integer)
    GC = Column("GC", Float)
    total_deduplicated = Column("total_deduplicated", Float)
    avg_sequence_length = Column("avg_sequence_length", Float)
    basic_statistics = Column("basic_sataistics", String)
    per_base_sequence_quality = Column("per_base_sequence_quality", String)
    per_tile_sequence_quality = Column("per_tile_sequence_quality", String)
    per_sequence_quality_scores = Column("per_sequence_quality_scores", String)
    per_base_sequence_content = Column("per_base_sequence_content", String)
    per_base_sequence_gc_content = Column("per_base_sequence_gc_content", String)
    per_base_n_content = Column("per_base_n_content", String)
    sequence_length_distribution = Column("sequence_length_distribution", String)
    sequence_duplication_levels = Column("sequence_duplication_levels", String)
    overrepresented_sequences = Column("overrepresented_sequences", String)
    adapter_content = Column("adapter_content", String)

    def __init__(self, FastQC_id, Filename, File_type, Encoding, Total_Sequences, Sequences_flagged_as_poor_quality, Sequence_length, GC, total_deduplicated, \
                 avg_sequence_length, basic_statistics, per_base_sequence_quality, per_tile_sequence_quality, per_sequence_quality_scores, per_base_sequence_content, \
                 per_base_sequence_gc_content, per_base_n_content, sequence_length_distribution, sequence_duplication_levels, overrepresented_sequences, adapter_content):
        self.FastQC_id = FastQC_id
        self.Filename - Filename
        self.File_type = File_type
        self.Encoding = Encoding
        self.Total_Sequences = Total_Sequences
        self.Sequences_flagged_as_poor_quality = Sequences_flagged_as_poor_quality
        self.Sequence_length = Sequence_length
        self.GC = GC
        self.total_deduplicated = total_deduplicated
        self.avg_sequence_length = avg_sequence_length
        self.basic_statistics = basic_statistics
        self.per_base_sequence_quality = per_base_sequence_quality
        self.per_tile_sequence_quality = per_tile_sequence_quality
        self.per_sequence_quality_scores = per_sequence_quality_scores
        self.per_base_sequence_content = per_base_sequence_content
        self.per_base_sequence_gc_content = per_base_sequence_gc_content
        self.per_base_n_content = per_base_n_content
        self.sequence_length_distribution = sequence_length_distribution
        self.sequence_duplication_levels = sequence_duplication_levels
        self.overrepresented_sequences = overrepresented_sequences
        self.adapter_content = adapter_content

    def __repr__(self):
         return f"({self.FastQC_id} {self.Filename} {self.File_type} {self.Encoding} {self.Total_Sequences} {self.Sequences_flagged_as_poor_quality} \
         {self.Sequence_length} {self.GC} {self.total_deduplicated} {self.avg_sequence_length} {self.basic_statistics} {self.per_base_sequence_quality} \
         {self.per_tile_sequence_quality} {self.per_sequence_quality_scores} {self.per_base_sequence_content} {self.per_base_sequence_gc_content} \
         {self.per_base_n_content} {self.sequence_length_distribution} {self.sequence_duplication_levels} {self.overrepresented_sequences} {self.adapter_content}"



engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)


def parse_none(dt):
    try:
        return parse(dt)
    except:
        return None
    
def prepare_Picard_HsMetrics(row):
    row["last_review"] = parse_none(row["last_review"])
    return Picard_HsMetrics(**row)

with open('multiqc_picard_HsMetrics.txt', encoding='utf-8', newline='') as csv_file:
    csvreader = csv.DictReader(csv_file, quotechar='"')

    picard_hsmetrics = [prepare_Picard_HsMetrics(row) for row in csvreader]

    session = Session()
    session.add_all(picard_hsmetrics)
    session.commit()